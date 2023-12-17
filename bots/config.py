from dotenv import load_dotenv
import os

load_dotenv()

P_CON = os.environ.get("P_CON")
EMAIL = os.environ.get("EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


BOT_TOKEN = os.environ.get("BOT_ID")
CHAT_LIST = [349653021]

create_files_query = '''
SELECT u.id, CONCAT(name, ' ', lastname) as fio,
 p.probability, s.subdivision,
d.department, ps.position,
CASE
    WHEN ub.is_view THEN 'Отслеживается'
    ELSE 'Не отслеживается'
    END
    as is_view
FROM public.users as u

JOIN 
(
SELECT DISTINCT user_id, FIRST_VALUE(probability) over (PARTITION BY user_id ORDER BY date DESC) as probability
FROM public.predicts
)
 as p on p.user_id = u.id 
 
JOIN 
(
SELECT subdivision_id as id, subdivision
FROM subdivisions
) as s on s.id = u.subdivision_id

JOIN 
(
SELECT department_id as id, department
FROM departments
) as d on d.id = u.department_id

JOIN positions as ps on ps.position_id = u.position_id

LEFT JOIN user_bots as ub on ub.user_id = u.id

WHERE role_id = 3


'''