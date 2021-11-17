""" Functions to return a dataframe containing free users data for n number of days"""


def free_users(n_days, connection):
    "return datafrae of free users for n_days"
    sqlQuery = (
        """SELECT u.Id as Iduser, u.Email as Email, u.CreateDate as CreateDate from skidos.User as u
            where SubscriptionExpire is null
            AND CreateDate >= CURDATE() - interval %s day AND CreateDate < CURDATE()"""
        % n
    )
    print(sqlQuery)
    sqlCursor = connection.cursor()
    sqlCursor.execute(sqlQuery)
    FreeUserData = pd.read_sql(sqlQuery, connection)
    return FreeUserData


def free_users_not_reachedlimit(n_days, connection):
    "find the list of free users who ReachedLimit for n days"
    sqlQuery = '''SELECT ul.IdUser as Iduser, ul.Date as Date, u.Email as Email FROM skidos.UserLimit as ul join skidos.User as u ON ul.IdUser = u.Id
                where u.SubscriptionExpire is null
                AND Date >= CURDATE() - interval 1 day AND Date < CURDATE() group by ul.IdUser having max(ul.Reached) = 1'''%n_days
    sqlCursor = connection.cursor()
    sqlCursor.execute(sqlQuery)
    FreeUserData = pd.read_sql(sqlQuery, connection)
    print(sqlQuery)
    return free_user_data 


def free_users_not_reachedlimit(n_days, connection):
    "find the list of free users who ReachedLimit for n days"
    sqlQuery = '''SELECT ul.IdUser as Iduser, ul.Date as Date, u.Email as Email FROM skidos.UserLimit as ul join skidos.User as u ON ul.IdUser = u.Id
                where u.SubscriptionExpire is null
                AND Date >= CURDATE() - interval 1 day AND Date < CURDATE() group by ul.IdUser having max(ul.Reached) = 0'''%n_days
    sqlCursor = connection.cursor()
    sqlCursor.execute(sqlQuery)
    FreeUserData = pd.read_sql(sqlQuery,connection)
    print(sqlQuery)
    return free_user_data 
