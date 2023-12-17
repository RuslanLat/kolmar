import pandas as pd


def make_features(df: pd.DataFrame) -> pd.DataFrame:
    if "name" in list(df.columns):
        df = df.drop(["employee_id", "name"], axis=1)
    else:
        df = df.drop(["employee_id"], axis=1)
    df["div_UseEmail"] = df["use_email_last"] / df["use_email_total"]
    df["div_answer_UseEmail"] = df["answer_last"] / df["use_email_last"]
    df["div_TotalLetters_answer"] = df["answer_last"] / df["total_letters_last"]
    df["div_sent_received_total"] = df["total_letters_total"] / df["received_total"]
    df["div_sent_received_last"] = df["total_letters_last"] / df["received_last"]
    return df


def make_predict(df: pd.DataFrame, load_model, df_test: pd.DataFrame) -> pd.DataFrame:
    # соеденяем предсказания
    hr_pred = pd.concat(
        [df[["employee_id"]], pd.DataFrame(load_model.predict(df_test))], axis=1
    )
    hr_pred = hr_pred.rename(columns={0: "dismiss"})
    # соеденяем вероятности
    proba_best = pd.DataFrame(load_model.predict_proba(df_test))
    proba_best = proba_best.rename(
        columns={0: "probability no", 1: "probability"}
    )
    proba_best = pd.concat([df[["employee_id"]], proba_best], axis=1)
    proba_best[["probability no", "probability"]] = proba_best[
        ["probability no", "probability"]
    ].applymap(lambda x: round(float(x * 100), 2))
    # объеденяем в один файл
    hr_pred = hr_pred.merge(proba_best, how="left", on="employee_id")

    return hr_pred
