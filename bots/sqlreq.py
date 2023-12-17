from sqlalchemy import create_engine
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import config as cn

con_str = cn.P_CON

# хардкод. каждый из отделов или департаментов будет иметь доступ только к данным своих подчиненных
# пока что строго заданы, после доработок данные по разрешениям будут браться из базы
temporary_permission = {
    -4087048084: 'Отдел №1',
    -4054526368: 'Департамент №2',
    -4084480739: 'Мастер чат'
}

master_chat = -4084480739

def check_permission(chat_id: int, params: str) -> str:
    if chat_id not in temporary_permission.keys():
        return 'denied'
    else:
        if chat_id != master_chat:
            if params is None:
                params = temporary_permission.get(chat_id)
            else:
                # хардкод по правам доступа
                if chat_id == -4087048084:
                    params = params if params == "Отдел №1" else None
                else:
                    cur_list = ["Департамент №2", "Отдел №3", "Отдел №4"]
                    params = params if params in cur_list else None
    return params

def predictions(query: str, req: str) -> str:
    engine = create_engine(con_str)
    df = pd.read_sql_query(query, con=engine)
    df = df.sort_values('probability', ascending=False)
    if req == 'top':
        df = df.head(3)
        res = ''
        for _, itm in df.iterrows():
            cur_res = f'<b>Сотрудник {itm["id"]}:</b> {itm["fio"]}, '
            cur_res += f' <b>вероятность</b>: {itm["probability"]}%'
            cur_res += f'{" (отслеживается)" if itm["is_view"] == "Отслеживается" else ""}'
            res += cur_res + '\n'
        return res
    else:
        df.to_csv(f'data/{req}.csv', index=False)
        return f'data/{req}.csv'

def user_list(query: str) -> str:
    engine = create_engine(con_str)
    df = pd.read_sql_query(query, con=engine)
    try:
        df = df.sample(10)
    except Exception as e:
        pass
    res = '<i>демо, до 10 случайных</i>\n'
    for _, itm in df.iterrows():
        cur_res = f'<b>Сотрудник {itm["id"]}:</b> {itm["fio"]}, <i>{itm["position"]}</i>'
        cur_res += f'{" (отслеживается)" if itm["is_view"] else ""}'
        res += cur_res + '\n'
    return res

def find_reqs(name: str) -> list[int, str]:
    engine = create_engine(con_str)
    query = f'''
        SELECT department_id as id
        FROM departments
        WHERE department = '{name}'
    '''
    find_id = pd.read_sql_query(query, con=engine)
    if not find_id.empty:
        return [find_id['id'][0], 'department_id']
    else:
        query = f'''
            SELECT subdivision_id as id
            FROM subdivisions
            WHERE subdivision = '{name}'
        '''
        find_id = pd.read_sql_query(query, con=engine)
        if not find_id.empty:
            return [find_id['id'][0], 'subdivision_id']
        else:
            return None

def follow(ids: int, is_view: bool = True) -> str:
    engine = create_engine(con_str)
    query = f'''
        SELECT CONCAT(name, ' ', lastname) as fio
        FROM users
        WHERE id = {ids} and position_id = 3
    '''
    df = pd.read_sql_query(query, con=engine)
    if df.empty:
        return 'Не найден сотрудник с таким ID (или является руководителем)'
    else:
        fio = df["fio"][0]
        # FIXLATER
        df = pd.read_sql_table('user_bots', con=engine)
        if ids not in df['user_id'].values:
            df.loc[-1, 'user_id'] = ids
            df.loc[-1, 'id'] = ids
        df.loc[df['user_id'] == ids, 'is_view'] = is_view
        df[['id', 'user_id']] = df[['id', 'user_id']].astype('int')
        df.to_sql('user_bots', con=engine, if_exists='replace', index=False)
        if is_view:
            return f'Сотрудник {ids} <i>{fio}</i> добавлен для отслеживания'
        else:
            return f'Сотрудник {ids} <i>{fio}</i> убран из отслеживания'

def pers_info(id: int) -> str:
    engine = create_engine(con_str)
    query = f'''
                SELECT u.id, CONCAT(name, ' ', lastname) as fio,
                p.probability, d.department, u.experience
                
                FROM public.users as u
                LEFT JOIN 
                (
                SELECT DISTINCT user_id, FIRST_VALUE(probability) over (PARTITION BY user_id ORDER BY date DESC) as probability
                FROM public.predicts
                )
                 as p on p.user_id = u.id 
                
                JOIN 
                (
                SELECT department_id as id, department
                FROM departments
                ) as d on d.id = u.department_id
                WHERE u.id = {id}
            '''
    df = pd.read_sql_query(query, con=engine)
    if df.empty:
        return 'Сотрудник не найден'
    else:
        res = df.loc[0]
        mess = f'<b>id:</b> {res["id"]} <b>ФИО</> {res["fio"]} - <i>{res["department"]}</i>\n'
        mess += f'<b>опыт работы:</b> {res["experience"]}'
        if res['probability']:
            mess += f'\n<b>шанс увольнения:</b> {res["probability"]}'
        return mess


def emails(filepath: str, to_: str) -> None:
    email = cn.EMAIL
    password = cn.EMAIL_PASSWORD
    try:
        dtq = str(pd.to_datetime('today').normalize().date()).replace('-', '')
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.ehlo()
        server.login(email, password)

        subject = f'Это письмо для {to_}'
        email_text = f'Отчет {dtq}'

        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = email
        message["To"] = email

        message.attach(MIMEText(email_text, _charset='utf-8'))

        file_path = filepath

        with open(file_path, "rb") as file:
            attachment = MIMEApplication(file.read(), _subtype="csv")
            attachment.add_header("Content-Disposition", f"attachment; filename=report{dtq}.csv")
            message.attach(attachment)

        server.sendmail(email, email, message.as_string())
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")
        pass
    finally:
        server.quit()


# в этой версии отчеты отправляются только HR и 2 руководителям
def send_reports(query: str, params: str) -> str:
    engine = create_engine(con_str)
    df = pd.read_sql_query(query, con=engine)
    df = df.sort_values('probability', ascending=False)
    if params == 'subdivisions':
        email = pd.read_sql_query('SELECT email FROM public.subdivisions WHERE subdivision_id = 1', con=engine)['email'][0]
    elif params == 'departments':
        email = pd.read_sql_query('SELECT email FROM public.departments WHERE department_id = 2', con=engine)['email'][0]
    else:
        email = 'hr@email'
    fname = 'data/report' + str(pd.to_datetime('today').normalize().date()).replace('-', '') + str(params) +'.csv'
    df.to_csv(fname, index=False)
    emails(fname, email)
    return fname
