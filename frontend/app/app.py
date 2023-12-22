import datetime
import requests
import joblib
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from PIL import Image
from streamlit_option_menu import option_menu
from src.aggrid_plot.plot_table import plot_change_table
from src.expanders.forms import (
    make_department_form,
    make_user_form,
    make_subdivision_form,
    make_role_form,
    make_position_form,
    make_job_form,
    make_uploaded_file_form,
    make_uploaded_file_demo_form,
    make_check_form,
    make_group_form,
)
from src.contacts.contact import show_conract, about
from src.db_requests.get_db import (
    get_departments_list,
    get_roles_list,
    get_subdivisions_list,
    get_positions_list,
    get_users_list,
    get_users_list_all,
    get_full_users_list,
    get_full_users_bot_list,
    get_group_list,
    get_insert_users,
    get_insert_email,
    get_insert_emails,
    get_insert_predict,
)
from src.features.features import make_features, make_predict

st.set_page_config(
    page_title="Угледобывающая компания «Колмар»",
    page_icon="app/images/favicon.ico",
    layout="wide",
)  # layout = "wide"


load_model = joblib.load("app/ml_model/yakytsk_model.pkl")

if "pred_button" not in st.session_state:
    st.session_state.pred_button = False

def on_click_load():
    st.session_state.pred_button = True


styles = {
    "container": {"padding": "0!important", "background-color": "#fafafa"},
    "icon": {
        "color": "#db0404",
        "font-size": "20px",
        "--hover-color": "#cccccc",
    },
    "nav-link": {
        "color": "black",
        "font-size": "15px",
        "text-align": "left",
        "margin": "0px",
        "--hover-color": "#cccccc",
    },
    "nav-link-selected": {
        "color": "#ffffff",
        "background-color": "#808080",
    },
}

sess = requests.Session()
# host = "http://127.0.0.1:8080/"
host = "http://89.232.160.71:8080/"
data = {"login": "user", "password": "user"}
sess.post(host + "user.login", json=data)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("app/css/style.css")


with st.sidebar:
    image = Image.open("app/images/logo.png")
    st.sidebar.image(image)
    st.write("##")
    selected = option_menu(
        None,
        [
            "О программе",
            "Персонал",
            "Прогнозирование",
            "Аналитика",
            "Контроль",
            "Контакты",
        ],
        icons=[
            "cast",
            "database",
            "list-task",
            "bar-chart",
            "clipboard2-check",
            "envelope-paper",
        ],
        menu_icon="cast",
        default_index=0,
        styles=styles,
    )
if selected == "О программе":
    about()
if selected == "Персонал":
    with st.expander("Департаменты"):
        (
            department_form,
            department,
            email,
            chat_number,
            department_radio,
            department_submitted,
        ) = make_department_form()
        col1, col2, col3 = st.columns((1, 3, 1))
        with col2:
            if (
                department_submitted
                and email
                and chat_number
                and department
                and department_radio == "Добавить"
            ):
                # client.post(
                #     host + "addresse.add", data={"city": city, "addresse": addresse}
                # )
                # client.post(
                #     host + "office.add", data={"city": city, "addresse": addresse}
                # )
                st.info("На время хакатона функция отключена", icon="ℹ️")
                # df = get_departments_list(sess=sess, host=host)
                # aggrid_department = plot_change_table()

            elif (
                department_submitted
                and email
                and chat_number
                and department
                and department_radio == "Удалить"
            ):
                # client.delete(
                #     host + "office.delete",
                #     params={"city": city, "addresse": addresse},
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1b")
                col2.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                not chat_number
                and department_submitted
                or not department
                and department_submitted
                or not email
                and department_submitted
            ):
                col2.error("Введите данные", icon="❌")
            else:
                df = get_departments_list(sess=sess, host=host)
                aggrid_department = plot_change_table(df, key="1a")

    with st.expander("Отделы"):
        (
            subdivision_form,
            subdivision,
            email,
            chat_number,
            subdivision_radio,
            subdivision_submitted,
        ) = make_subdivision_form()
        col1, col2, col3 = st.columns((1, 3, 1))
        with col2:
            if (
                subdivision_submitted
                and email
                and chat_number
                and subdivision
                and subdivision_radio == "Добавить"
            ):
                # client.post(
                #     host + "addresse.add", data={"city": city, "addresse": addresse}
                # )
                # client.post(
                #     host + "office.add", data={"city": city, "addresse": addresse}
                # )
                st.info("На время хакатона функция отключена", icon="ℹ️")
                # df = get_departments_list(sess=sess, host=host)
                # aggrid_department = plot_change_table()

            elif (
                subdivision_submitted
                and email
                and chat_number
                and subdivision
                and subdivision_radio == "Удалить"
            ):
                # client.delete(
                #     host + "office.delete",
                #     params={"city": city, "addresse": addresse},
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1b")
                col2.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                not chat_number
                and subdivision_submitted
                or not subdivision
                and subdivision_submitted
                or not email
                and subdivision_submitted
            ):
                col2.error("Введите данные", icon="❌")
            else:
                df = get_subdivisions_list(sess=sess, host=host)
                aggrid_subdivision = plot_change_table(df, key="2a")
    with st.expander("Персонал"):
        selected2 = option_menu(
            None,
            ["Должности", "Роли", "Сотрудники", "Штат"],
            icons=["layers", "view-list", "people", "diagram-3"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles=styles,
        )
        if selected2 == "Должности":
            (
                position_form,
                position,
                position_radio,
                position_submitted,
            ) = make_position_form()
            col1, col2, col3 = st.columns((1, 3, 1))
            with col2:
                if position_submitted and position and position_radio == "Добавить":
                    # client.post(
                    #     host + "addresse.add", data={"city": city, "addresse": addresse}
                    # )
                    # client.post(
                    #     host + "office.add", data={"city": city, "addresse": addresse}
                    # )
                    st.info("На время хакатона функция отключена", icon="ℹ️")
                    # df = get_departments_list(sess=sess, host=host)
                    # aggrid_department = plot_change_table()

                elif position_submitted and position and position_radio == "Удалить":
                    # client.delete(
                    #     host + "office.delete",
                    #     params={"city": city, "addresse": addresse},
                    # )
                    # df = get_office_list()
                    # aggrid = plot_table(df, key="1b")
                    col2.info("На время хакатона функция отключена", icon="ℹ️")
                elif not position and position_submitted:
                    col2.error("Введите данные", icon="❌")
                else:
                    df = get_positions_list(sess=sess, host=host)
                    aggrid_position = plot_change_table(df, key="3a")

        if selected2 == "Роли":
            role_form, role, role_radio, role_submitted = make_role_form()
            col1, col2, col3 = st.columns((1, 3, 1))
            with col2:
                if role_submitted and role and role_radio == "Добавить":
                    # client.post(
                    #     host + "addresse.add", data={"city": city, "addresse": addresse}
                    # )
                    # client.post(
                    #     host + "office.add", data={"city": city, "addresse": addresse}
                    # )
                    st.info("На время хакатона функция отключена", icon="ℹ️")
                    # df = get_departments_list(sess=sess, host=host)
                    # aggrid_department = plot_change_table()

                elif role_submitted and role and role_radio == "Удалить":
                    # client.delete(
                    #     host + "office.delete",
                    #     params={"city": city, "addresse": addresse},
                    # )
                    # df = get_office_list()
                    # aggrid = plot_table(df, key="1b")
                    col2.info("На время хакатона функция отключена", icon="ℹ️")
                elif not role and role_submitted:
                    col2.error("Введите данные", icon="❌")
                else:
                    df = get_roles_list(sess=sess, host=host)
                    aggrid_role = plot_change_table(df, key="4a")

        if selected2 == "Сотрудники":
            (
                user_form,
                name,
                lastname,
                male,
                age,
                experience,
                email,
                chat_number,
                user_radio,
                user_submitted,
            ) = make_user_form()
            if (
                user_submitted
                and name
                and lastname
                and male
                and email
                and chat_number
                and user_radio == "Добавить"
            ):
                # client.post(
                #     host + "addresse.add", data={"city": city, "addresse": addresse}
                # )
                # client.post(
                #     host + "office.add", data={"city": city, "addresse": addresse}
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1a")
                st.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                user_submitted
                and name
                and lastname
                and male
                and email
                and chat_number
                and user_radio == "Удалить"
            ):
                # client.delete(
                #     host + "office.delete",
                #     params={"city": city, "addresse": addresse},
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1b")
                st.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                not name
                and user_submitted
                and not lastname
                and not male
                and not email
                and not chat_number
            ):
                st.error("Введите данные", icon="❌")
            else:
                df = get_users_list(sess=sess, host=host)
                aggrid_user = plot_change_table(df, key="5a")

        if selected2 == "Штат":
            df_user = get_users_list(sess=sess, host=host)
            df_user["full_name"] = df_user["Имя"] + " " + df_user["Фамилия"]
            df_department = get_departments_list(sess=sess, host=host)
            df_subdivision = get_subdivisions_list(sess=sess, host=host)
            df_role = get_roles_list(sess=sess, host=host)
            df_position = get_positions_list(sess=sess, host=host)
            (
                job_form,
                full_name,
                department_job,
                subdivision_job,
                position_job,
                role_job,
                job_form_radio,
                job_form_submitted,
            ) = make_job_form(
                full_name_option=df_user["full_name"].unique().tolist(),
                department_option=df_department["Департамент"].unique().tolist(),
                subdivision_option=df_subdivision["Отдел"].unique().tolist(),
                position_option=df_position["Должность"].unique().tolist(),
                role_option=df_role["Роль"].unique().tolist()
            )
            if (
                job_form_submitted
                and full_name
                and department_job
                and subdivision_job
                and position_job
                and role_job
                and job_form_radio == "Добавить"
            ):
                # client.post(
                #     host + "addresse.add", data={"city": city, "addresse": addresse}
                # )
                # client.post(
                #     host + "office.add", data={"city": city, "addresse": addresse}
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1a")
                st.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                job_form_submitted
                and full_name
                and department_job
                and subdivision_job
                and position_job
                and role_job
                and job_form_radio == "Удалить"
            ):
                # client.delete(
                #     host + "office.delete",
                #     params={"city": city, "addresse": addresse},
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1b")
                st.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                not full_name
                and job_form_submitted
                and not department_job
                and not subdivision_job
                and not position_job
                and not role_job
            ):
                st.error("Введите данные", icon="❌")
            else:
                df = get_users_list_all(sess=sess, host=host)
                aggrid_user_all = plot_change_table(df, key="6a")
    with st.expander("Группы"):
        (
            group_form,
            group,
            group_radio,
            group_submitted,
        ) = make_group_form()
        col1, col2, col3 = st.columns((1, 3, 1))
        with col2:
            if (
                group_submitted
                and group
                and group_radio == "Добавить"
            ):
                # client.post(
                #     host + "addresse.add", data={"city": city, "addresse": addresse}
                # )
                # client.post(
                #     host + "office.add", data={"city": city, "addresse": addresse}
                # )
                st.info("На время хакатона функция отключена", icon="ℹ️")
                # df = get_departments_list(sess=sess, host=host)
                # aggrid_department = plot_change_table()

            elif (
                group_submitted
                and group
                and group_radio == "Удалить"
            ):
                # client.delete(
                #     host + "office.delete",
                #     params={"city": city, "addresse": addresse},
                # )
                # df = get_office_list()
                # aggrid = plot_table(df, key="1b")
                col2.info("На время хакатона функция отключена", icon="ℹ️")
            elif (
                not group
                and group_submitted
            ):
                col2.error("Введите данные", icon="❌")
            else:
                df = get_group_list(sess=sess, host=host)
                aggrid_group = plot_change_table(df, key="2b")
if selected == "Прогнозирование":
    st.markdown(
        '<h2 style="text-align: center; color: blac;"> Прогнозирование увольнения на основе вовлеченности сотрудника </h2>',
        unsafe_allow_html=True,
    )
    st.write("##")
    on = st.toggle("Демонстративный режим")
    if not on:
        uploaded_file_form, uploaded_file = make_uploaded_file_form()
        current_time = str(datetime.datetime.now())
    else:
        uploaded_file_form, uploaded_file, day, uploaded_button = make_uploaded_file_demo_form()
        current_time = f"{day} 10:00:00"
    if uploaded_file:
        st.write(
        f"""
        📌 Имя файла: {uploaded_file.name}""")
        df = pd.read_csv(uploaded_file)
        adgrid_df = plot_change_table(df, key="df")
        df_test = make_features(df)
        pred_df = make_predict(df=df, load_model=load_model, df_test=df_test)
        full_users_df = get_full_users_list(host=host, sess=sess)
        adgrid_pred_show = pred_df.merge(full_users_df, left_on="employee_id", right_on="id")
        adgrid_pred_show = adgrid_pred_show.sort_values(by="probability", ascending=False)
        pred_button = st.button("Предсказать", on_click=on_click_load, disabled=False)
        if pred_button:
            adgrid_pred_df = plot_change_table(adgrid_pred_show.iloc[:,[0, 5, 6, 7, 8, 9, 1, 3]], key="pred")
        if st.session_state.pred_button:
            col1, col2, col3 = st.columns((2, 1, 1))
            with col1:
                send_form = st.form("send_form")
                send_form.write("Сохранение результатов")
                stat = send_form.checkbox("Сохранить статистику по переписке в базу данных",
                                    value=True,
                                    key="stat",
                                    help="при выборе опции данные со статистикой почтовой переписки сохраняться в базу данных")

                predict_data = send_form.checkbox("Сохранить результат предсказания в базу данных",
                                   value=True,
                                    key="predict_data",
                                    help="при выборе опции данные с предсказаниями сохраняться в базу данных")

                # send_email = send_form.checkbox("Разослать результат предсказания руководителям на e-mail и в telegram",
                #                     value=True,
                #                     key="send_email",
                #                     help="при выборе опции данные с предсказаниями рассылаются на e-mail и в telegram руководителям")

                send_form_button = send_form.form_submit_button("Сохранить")
                if send_form_button:
    
                    if stat:
                        df_insert = df.iloc[:,[0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]]
                        df_insert.rename(columns={"employee_id" : "user_id"}, inplace=True)
                        df_insert.insert(loc= 1 , column='date', value=[current_time for _ in range(len(df_insert))])
                        emails = list(df_insert.T.to_dict().values())
                        data = {"emails" : emails}
                        r = sess.post(host + "email.add.all", json=data)
                    if predict_data:
                        df_predict = pred_df.iloc[:,[0, 1, -1]]
                        df_predict.rename(columns={"employee_id" : "user_id"}, inplace=True)
                        df_predict.insert(loc= 1 , column='date', value=[current_time for _ in range(len(df_predict))])
                        predicts = list(df_predict.T.to_dict().values())
                        data_predict = {"predicts" : predicts}
                        r = sess.post(host + "predict.add.all", json=data_predict)
                    # if send_email:
                    #     st.write("Почта")
                    #     print("Почта")
                    

if selected == "Аналитика":
    st.markdown(
        '<h2 style="text-align: center; color: blac;"> Анализ прогнозирования увольнения<br>на основе вовлеченности сотрудника </h2>',
        unsafe_allow_html=True,
    )
    st.write(
        '<iframe frameborder="0" src="https://datalens.yandex/qd5f3pdgqoy6f" width="100%" height=1400></iframe>',
        unsafe_allow_html=True,
    )

if selected == "Контроль":
    users_is_view_list = get_full_users_bot_list(host=host, sess=sess)
    full_name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11 = make_check_form(user_list=users_is_view_list)
    df = get_group_list(sess=sess, host=host)
    qroup_option = list(df["Комментарий"].unique())
    col1, col2, col3 = st.columns((1,4,1))
    qroup_select = col2.selectbox(
            label="А/B группа тестирования",
            options=qroup_option,
            placeholder="Выберите группу А/B тестирования ...",
            index=None,
            help="выберите группу А/B тестирования",
            key="qroup_select",
        )
    save_check = col2.button("Сохранить")
    if save_check and full_name and q1 and q2 and q3 and q4 and q5 and q6 and q7 and q8 and q9 and q10 and q11:
        r = sess.post(host + "stimul.add",
                    json={"name" : full_name.split()[0],
                        "lastname" : full_name.split()[1],
                        "q1" : q1,
                        "q2" : q2,
                        "q3" : q3,
                        "q4" : q4,
                        "q5" : q5,
                        "q6" : q6,
                        "q7" : q7,
                        "q8" : q8,
                        "q9" : q9,
                        "q10" : q10,
                        "q11" : q11})
    else:
        col2.error("Вы ничего не выбрали", icon="❌")

if selected == "Контакты":
    show_conract()
