import streamlit as st

def make_department_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        department_form = st.form("department_form")
        department_form.write("Добавить/удалить департамент")
        department = department_form.text_input(
            label="Наименование департамента",
            placeholder="Введите наименование департамента ...",
            help="введите наименование департамента",
            key="department",
        )
        email = department_form.text_input(
            label="E-mail",
            placeholder="Введите электронную почту ...",
            help="введите электронную почту",
            key="email",
        )
        chat_number = department_form.text_input(
            label="ID чата в telegram",
            placeholder="Введите ID чата в telegram ...",
            help="введите ID чата в telegram",
            key="chat_number",
        )
        department_radio = department_form.radio(
            "Добавить/удалить",
            ["Добавить", "Удалить"],
            horizontal=True,
            label_visibility="collapsed",
        )
        department_submitted = department_form.form_submit_button("сохранить")

    return (
        department_form,
        department,
        email,
        chat_number,
        department_radio,
        department_submitted,
    )


def make_subdivision_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        subdivision_form = st.form("subdivision_form")
        subdivision_form.write("Добавить/удалить отдел")
        subdivision = subdivision_form.text_input(
            label="Наименование отдела",
            placeholder="Введите наименование отдела ...",
            help="введите наименование отдела",
            key="subdivision",
        )
        email = subdivision_form.text_input(
            label="E-mail",
            placeholder="Введите электронную почту ...",
            help="введите электронную почту",
            key="email_sub",
        )
        chat_number = subdivision_form.text_input(
            label="ID чата в telegram",
            placeholder="Введите ID чата в telegram ...",
            help="введите ID чата в telegram",
            key="chat_number_sub",
        )
        subdivision_radio = subdivision_form.radio(
            "Добавить/удалить",
            ["Добавить", "Удалить"],
            horizontal=True,
            label_visibility="collapsed",
        )
        subdivision_submitted = subdivision_form.form_submit_button("сохранить")

    return (
        subdivision_form,
        subdivision,
        email,
        chat_number,
        subdivision_radio,
        subdivision_submitted,
    )


def make_role_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        role_form = st.form("role_form")
        role_form.write("Добавить/удалить роль")
        role = role_form.text_input(
            label="Наименование роли",
            placeholder="Введите наименование роли ...",
            help="введите наименование роли",
            key="role",
        )
        role_radio = role_form.radio(
            "Добавить/удалить",
            ["Добавить", "Удалить"],
            horizontal=True,
            label_visibility="collapsed",
        )
        role_submitted = role_form.form_submit_button("сохранить")

    return role_form, role, role_radio, role_submitted


def make_position_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        position_form = st.form("position_form")
        position_form.write("Добавить/удалить должность")
        position = position_form.text_input(
            label="Наименование должности",
            placeholder="Введите наименование должности ...",
            help="введите наименование должности",
            key="position",
        )
        position_radio = position_form.radio(
            "Добавить/удалить",
            ["Добавить", "Удалить"],
            horizontal=True,
            label_visibility="collapsed",
        )
        position_submitted = position_form.form_submit_button("сохранить")

    return position_form, position, position_radio, position_submitted


def make_user_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        user_form = st.form("user_form")
        user_form.write("Добавить/удалить сотрудника")
        name = user_form.text_input(
            label="Имя сотрудника",
            placeholder="Введите имя сотрудника ...",
            help="введите имя сотрудника",
            key="name",
        )
        lastname = user_form.text_input(
            label="Фамилия сотрудника",
            placeholder="Введите фамилию сотрудника ...",
            help="введите фамилию сотрудника",
            key="lastname",
        )
        male = user_form.selectbox(
            label="Пол",
            options=["мужчина", "женщина"],
            index=None,
            placeholder="Выбирете пол сотрудника... ",
            help="выбирете пол сотрудника",
            key="male",
        )
        col4, col5 = user_form.columns(2)
        age = col4.number_input(
            label="Возраст",
            min_value=18,
            max_value=70,
            step=1,
            help="введите возраст сотрудника",
            key="age",
        )
        experience = col5.number_input(
            label="Стаж работы",
            min_value=0,
            max_value=1000,
            step=1,
            help="введите стаж работы сотрудника",
            key="experience",
        )
        email = user_form.text_input(
            label="E-mail",
            placeholder="Введите электронную почту ...",
            help="введите электронную почту",
            key="email_user",
        )
        chat_number = user_form.text_input(
            label="ID telegram",
            placeholder="Введите ID telegram ...",
            help="введите ID telegram",
            key="chat_number_user",
        )
        user_radio = user_form.radio(
            "Добавить/удалить",
            ["Добавить", "Удалить"],
            horizontal=True,
            label_visibility="collapsed",
        )
        user_submitted = user_form.form_submit_button("сохранить")

    return (
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
    )


def make_job_form(
    full_name_option,
    department_option,
    subdivision_option,
    position_option,
    role_option,
):
    col1, col2, col3 = st.columns(3)
    with col2:
        job_form = st.form("job_form")
        job_form.write("Добавить/удалить сотрудника")

        full_name = job_form.selectbox(
            label="Cотрудник",
            options=full_name_option,
            placeholder="Выбирете сотрудника ...",
            index=None,
            help="выбирете сотрудника",
            key="full_name",
        )
        department_job = job_form.selectbox(
            label="Департамент",
            options=department_option,
            placeholder="Выбирете департамент ...",
            index=None,
            help="выбирете департамент",
            key="department_job",
        )
        subdivision_job = job_form.selectbox(
            label="Отдел",
            options=subdivision_option,
            placeholder="Выбирете отдел ...",
            index=None,
            help="выбирете отдел",
            key="subdivision_job",
        )
        position_job = job_form.selectbox(
            label="Должность сотрудника",
            options=position_option,
            index=None,
            placeholder="Выбирете должность сотрудника ...",
            help="выбирете должность сотрудника",
            key="position_job",
        )
        role_job = job_form.selectbox(
            label="Роль сотрудника",
            options=role_option,
            index=None,
            placeholder="Выбирете роль сотрудника ...",
            help="выбирете роль сотрудника",
            key="role_job",
        )
        job_form_radio = job_form.radio(
            "Добавить/удалить",
            ["Добавить", "Удалить"],
            horizontal=True,
            label_visibility="collapsed",
        )
        job_form_submitted = job_form.form_submit_button("сохранить")

    return (
        job_form,
        full_name,
        department_job,
        subdivision_job,
        position_job,
        role_job,
        job_form_radio,
        job_form_submitted,
    )


def make_uploaded_file_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        uploaded_file_form = st.form("uploaded_file_form")
        uploaded_file_form.write("Данные с почтовой перепиской")
        uploaded_file = uploaded_file_form.file_uploader(
            "Загрузка файла", type=["csv"], help="загрузите файл"
        )
        uploaded_file_form.form_submit_button("Загрузить")
        if uploaded_file:
            st.success("Файл успешно загружен", icon="✅")
        else:
            st.error("Вы ничего не выбрали", icon="❌")

    return uploaded_file_form, uploaded_file


def make_uploaded_file_demo_form():
    col1, col2, col3 = st.columns(3)
    with col2:
        uploaded_file_form = st.form("uploaded_file_form_demo")
        uploaded_file_form.write("Данные с почтовой перепиской")
        day = uploaded_file_form.date_input(
            label="Текущий день",
            format="YYYY-MM-DD",
            help="выбирете текущий день",
        )
        uploaded_file = uploaded_file_form.file_uploader(
            "Загрузка файла", type=["csv"], help="загрузите файл"
        )
        uploaded_button = uploaded_file_form.form_submit_button("Загрузить")
        if uploaded_file:
            st.success("Файл успешно загружен", icon="✅")
        else:
            st.error("Вы ничего не выбрали", icon="❌")

    return uploaded_file_form, uploaded_file, day, uploaded_button


def make_check_form():
    st.markdown(
        '<h2 style="text-align: center; color: blac;"> Чек лист<br>для работы с сотрудниками под риском увольнения </h2>',
        unsafe_allow_html=True,
    )
    st.write("##")
    col1, col2, col3 = st.columns((1,4,1))
    col2.write("Выявить причины неудовлестворенности работой")
    col2.text_area(label="ответ сотрудника", key="q1")
    col2.divider()
    col2.write("Выявить потребности, которые не достаточноном количестве удовлетворяются у сотрудника")
    col2.text_area(label="ответ сотрудника", key="q2")
    col2.divider()
    col2.write("При какких обстоятельствах сотрудник изменит свое отношение к компании")
    col2.text_area(label="ответ сотрудника", key="q3")
    col2.divider()
    col2.write("Нужна ли сотруднику помощь в решении проблем, которые помогут ему остаться в компании")
    col2.text_area(label="ответ сотрудника", key="q4")
    col2.divider()
    col2.write("Основные причины недовольства работой в компании")
    col2.text_area(label="ответ сотрудника", key="q5")
    col2.divider()
    col2.write("Что бы сотрудник хотел изменить в своем рабочем процессе")
    col2.text_area(label="ответ сотрудника", key="q6")
    col2.divider()
    col2.write("Что бы сотрудник хотел изменить на рабочем месте")
    col2.text_area(label="ответ сотрудника", key="q7")
    col2.divider()
    col2.write("Когда сотруднику последний раз повышали з/п")
    col2.text_area(label="ответ сотрудника", key="q8")
    col2.divider()
    col2.write("Когда сотруднику последний раз выплачивали премию")
    col2.text_area(label="ответ сотрудника", key="q9")
    col2.divider()
    col2.write("Как сотрудник оценивает результаты своего труда в компании (10 бальная шкала)")
    col2.text_area(label="ответ сотрудника", key="q10")
    col2.divider()
    col2.write("Чего хочет добиться сотрудник в работе")
    col2.text_area(label="ответ сотрудника", key="q11")
