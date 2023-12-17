[Обратно в README:leftwards_arrow_with_hook:](README.md)

## СОПРОВОДИТЕЛЬНАЯ ДОКУМЕНТАЦИЯ

### 1. Структура данных таблиц СУБД

База данных реализована в PostgreSQL

(параметры доступа)
- host: 89.232.167.79
- port: 5432
- user: root
- password: Rtunb892
- database: postgres

**PostgreSQL** — это объектно-реляционная система управления базами данных (ORDBMS), наиболее развитая из открытых СУБД в мире. Имеет открытый исходный код и является альтернативой коммерческим базам данных.

[nosqldbm.xml](nosqldbm.xml) - описания модели данных, [сервис](https://nosqldbm.ru/) для просмотра в интерактивном режиме



![nosqldbm](images/nosqldbm.png)


| Таблицы           | Наименование таблиц          |
|-------------------|:----------------------------:|
| admins            | админ                        | 
| users             | сотрудники                   |
| departments       | департаменты                 | 
| subdivisions      | отделы                       | 
| roles             | роли                         | 
| positions         | должности                    | 
| emails            | письма                       | 
| predicts          | предсказания                 | 
| ratings           | рейтинг                      | 
| user_bots         | служебная таблица для бота   | 
| department_bots   | служебная таблица для бота   | 
| subdivision_bots  | служебная таблица для бота   | 


### 2. Модуль оповещений и рассылки отчетов (Telegram  bot)

* [Telegram bot HR](https://t.me/+-xqRcI592AhiNTYy)
* [Telegram bot Департамента](https://t.me/+-xqRcI592AhiNTYy)
* [Telegram bot Отдела](https://t.me/+3uNhuYjW8OkwNzhi)

#### 2.1 Команды, доступные только для HR чата

***/рассылка***
	отправляет в чат и почту HR, а также ответственным руководителям файл **.csv** с отчётом  - вероятность увольнения по каждому сотруднику, находящемуся в подчинении. HR получает отчет по всем сотрудникам.  
*Примечание:* на текущий момент все отчеты отправляются на технический email. При этом данные email берутся из таблицы департаментов и отделов, соответсвующие адреса отображаются в заголовке письма ( kolmar.hr@yandex.ru )
 
***/отслеживать \<id>***
	добавляет к отслеживанию сотрудника с ID = \<id> - отображается на дашборде.

***/неотслеживать \<id>***
	убирает из отслеживания

***/инфо <id>***
	показывает краткую информацию о сотруднике с ID = \<id>

#### 2.2 Команды для всех чатов

**Правила доступа:**
	* Чат отдела имеет доступ к данным только своего отдела
	* Чат депортамента имеет доступ к данным всех отделов, входящих в состав департамента

***/отчет***
***/отчет <название отдела или департамента>***
	Если указано название отдела/департамента, бот отправит файл с данными по сотрудникам отдела/департамента с указанием шанса уволиться, если нет, отправит файл со всеми данными, к которым есть доступ

***/топ3***
***/топ3 <название отдела или департамента>***
Если указано название отдела/департамента, бот отправит файл с данными по ТОП-3 сотрудникам отдела/департамента с максимальным шансом уволиться, если нет, отправит файл со всеми данными ТОП-3 сотрудников с максимальным шансом уволиться, к которым есть доступ

***/список***
***/список <название отдела или департамента>***
	Если указано название отдела/департамента, бот отправит файл с данными по сотрудникам отдела/департамента, если нет, отправит файл со всеми данными, к которым есть доступ


***Комментарии:***
Данные в информационных отчетах и файлах демонстарционные, при необходимости можно доработать и выводить любые необходимые поля, которые есть в БД

#### 2.3 Технические команды:

***/номерчата***
 отображает номер текущего чата, чтоб можно было ему дать доступ

***/команды***
список команд

#### 2.4 В реализации:

Для HR чата сделать команду, которая будет давать права доступа для других чатов
На текущий момент все доступы "захардкожены"”", далее все доступы могут быть доступны на основе данных из БД

### 3. Описание структуры входных и выходных данных

#### 3.1 Входные данные

Файл в формате **CSV** разделитель **,**

[Обазец файла](data/test_1_day.csv) - для загрузки в модель


| Наименование признака          | Значение признака                                                          | Тип данных |
|--------------------------------|----------------------------------------------------------------------------|:----------:|
| employee_id                    | id сотрудника                                                              | int64      | 
| male                           | пол                                                                        | int64      | 
| age                            | возраст                                                                    | int64      | 
| experience                     | опыт в днях                                                                | int64      | 
| use_email_total                | вход в почту итого за анализируемый период                                 | int64      | 
| active_use_email               | количество активных дней использования почты за анализируемый период       | int64      | 
| use_email_last                 | вход в почту итого за последний месяц перед предсказанием                  | int64      | 
| out_work_internal_email_total  | отправка писем итого внутри компании вне рабочего времени                  | int64      | 
| out_work_internal_email_last   | отправка писем последний месяц внутри компании вне рабочего времени        | int64      | 
| out_work_external_email_total  | отправка писем итого внешним компаниям вне рабочего времени                | int64      | 
| out_work_external_email_last   | отправка писем последний месяц внешним компаниям вне рабочего времени      | int64      | 
| cnt_days_pause_total           | итого количество дней между получением письма и его прочтением             | int64      | 
| cnt_days_pause_last 	          | количество дней между получением письма и его прочтением в послений месяц  |	int64      |
| cnt_4hours_later_total         | количество писем итого прочитанных более чем через 4 часа	                 |	int64      |
| cnt_4hours_later_last 	        | количество писем в последний месяц прочитанных более чем через 4 часа	     |	int64      |
| total_letters_total 	          | итого отправленных писем	                                                  |	int64      |
| total_letters_last	            | количество писем отправленных в последний месяц	                           |	int64      |
| received_total	                | итого полученных сообщений	                                                |	int64      |
| received_last            	     | полученные сообщения в последний месяц	                                    |	int64      |
| answer_total 	                 | итого сообщенний на который направлен ответ	                               |	int64      |
| answer_last 	                  | сообщенния за последний месяц на который направлен ответ	                  |	int64      |
| out_work_email_total	          | отправка писем итого вне рабочего времени	                                 |	int64      |
| out_work_email_last	           | отправка писем последний месяц вне рабочего времени	                       |	int64      |
| external_email_total           |	отправка писем итого внешним компаниям	                                    |	int64      |
| external_email_last 	          | отправка писем последний месяц внутри компании	                            |	int64      |
| internal_email_total           |	отправка писем итого внутри компании	                                      |	int64      |
| internall_email_last           | отправка писем последний месяц внутри компании	                            |	int64      |
| cnt_addressees	                | количество адресатов в отправляемых сообщениях;	                           |	int64      |
| cnt_address_copy_total	        | количество сообщений с адресатами в поле "копия", всего за период	         |	int64      |
| cnt_address_copy_last	         | количество сообщений с адресатами в поле "копия", в последний месяц	       |	int64      |
| cnt_address_hidden_copy_total	 | количество сообщений с адресатами в поле «скрытая копия» итого за период	  |	int64      |
| cnt_address_hidden_copy_last	  | количество сообщений с адресатами в поле «скрытая копия» в последний месяц |	int64      |
| div_bytes_emails	              | отношение объема в байтах получаемых и отправляемых сообщений	             | float64    |
| cnt_question_incoming	         | количество входящих сообщений, имеющих вопросительные знаки в тексте, но на которые не был направлен ответ.      | int64      |                                      
| cnt_text_mean_total	           | среднее количество символов в отправлемых письмах за аналищируемый период	 | float64    |
| cnt_text_mean_last	            | среднее количество символов в отправлемых письмах в последний месяц	       | float64    | 


#### 3.2 Выходные данные

| Наименование признака          | Значение признака                                                          | Тип данных |
|--------------------------------|----------------------------------------------------------------------------|:----------:|
| employee_id                    | id сотрудника                                                              | int64      | 
| name                           | имя                                                                        | object     | 
| lastname                       | фамилия                                                                    | object     | 
| department                     | департамент                                                                | object     | 
| subdivision                    | отдел                                                                      | object     | 
| position                       | должность                                                                  | object     | 
| dismiss                        | метка класса (1 - уволить, 0 - не уволить )                                | int64      | 
| probability                    | вероятность увольнения                                                     | float64    | 

Доступна выгрузка выходных данных в файл
* в формате **CSV** разделитель **,**
* в формате **XLSX** MS Office
