import pandas as pd


def get_roles_list(host, sess):
    r = sess.get(host + "role.list")

    df = pd.DataFrame(r.json()["data"]["roles"]).rename(
        columns={"role_id": "ID роли", "role": "Роль"}
    )

    return df


def get_positions_list(host, sess):
    r = sess.get(host + "position.list")

    df = pd.DataFrame(r.json()["data"]["positions"]).rename(
        columns={"position_id": "ID должности", "position": "Должность"}
    )

    return df


def get_departments_list(host, sess):
    r = sess.get(host + "department.list")

    df = pd.DataFrame(r.json()["data"]["departments"]).rename(
        columns={"department_id": "ID департамента", "department": "Департамент"}
    )

    return df


def get_subdivisions_list(host, sess):
    r = sess.get(host + "subdivision.list")

    df = pd.DataFrame(r.json()["data"]["subdivisions"]).rename(
        columns={"subdivision_id": "ID отдела", "subdivision": "Отдел"}
    )

    return df


def get_users_list(host, sess):
    r = sess.get(host + "user.list")
    male_data = {0: "Женский", 1: "Мужской"}

    df = pd.DataFrame(r.json()["data"]["users"]).iloc[:, [0, 1, 2, 3, 4, 5, -3, -2]]
    df["male"] = df["male"].astype("int")
    df["male"] = df["male"].map(male_data)
    df.rename(
        columns={
            "id": "ID сотрудника",
            "name": "Имя",
            "lastname": "Фамилия",
            "male": "Пол",
            "age": "Возраст",
            "experience": "Стаж работы",
        },
        inplace=True,
    )

    return df


def get_users_list_all(host, sess):
    r = sess.get(host + "user.list")

    df = (
        pd.DataFrame(r.json()["data"]["users"])
        .iloc[:, [0, 1, 2, 7, 8, 9, 10]]
        .rename(
            columns={
                "id": "ID сотрудника",
                "name": "Имя",
                "lastname": "Фамилия",
                "department_id": "Департамент",
                "subdivision_id": "Отдел",
                "position_id": "Должность",
                "role_id": "Роль",
            }
        )
    )

    return df


def get_insert_users(host, sess, data):
    sess.post(host + "user.insert.add", data=data)


def get_insert_email(host, sess, data):
    sess.post(host + "email.add", data=data)


def get_insert_emails(host, sess, data):
    sess.post(host + "email.add.all", json=data)


def get_insert_predict(host, sess, data):
    sess.post(host + "predict.add", data=data)

def get_full_users_list(host, sess):
    r = sess.get(host + "user.full.list")
    df = pd.DataFrame(r.json()["data"]["users"]).iloc[:, [0, 1, 2, 7, 8, 9]]

    return df


def get_full_users_bot_list(host, sess):
    r = sess.get(host + "user.full.bot.list")
    df = pd.DataFrame(r.json()["data"]["users"])

    df["full_name"] = df["name"] + " " + df["lastname"]

    return df["full_name"].to_list()

def get_group_list(host, sess):
    r = sess.get(host + "group.list")
    df = pd.DataFrame(r.json()["data"]["groups"]).rename(
        columns={"group_id": "А/B группа тестирования", "group": "Комментарий"}
    )

    return df