""" Functions to return a dataframe containing free users data for n number of days"""

def free_users(n):
    "return datafrae of free users for n_days"
    free_users = []
    sqlQuery = '''SELECT u.Id as Iduser, u.Email as Email, u.CreateDate as CreateDate from skidos.User as u where SubscriptionExpire is null AND CreateDate >= CURDATE() - interval %s day AND CreateDate < CURDATE()'''%n
    print(sqlQuery)
    sqlCursor = connection.cursor()
    sqlCursor.execute(sqlQuery)
    FreeUserData = pd.read_sql(sqlQuery,connection)
    return FreeUserData

def free_users_ReachedLimit(n):
    "find the list of free users who ReachedLimit for n days"
    sqlQuery = '''SELECT ul.Id as Iduser, ul.Date as Date, u.Email as Email FROM skidos.UserLimit as ul JOIN skidos.User as u ON ul.Id = u.Id where SubscriptionExpire is null and Reached=1 AND Date >= CURDATE() -  interval %s day AND Date < CURDATE()'''%n
    print(sqlQuery)
    sqlCursor = connection.cursor()
    sqlCursor.execute(sqlQuery)
    FreeUserData = pd.read_sql(sqlQuery,connection)
    return FreeUserData

def free_users_Not_ReachedLimit(n):
    "find the list of free users who don't ReachedLimit for n days"
    sqlQuery = '''SELECT ul.Id as Iduser, ul.Date as Date, u.Email as Email FROM skidos.UserLimit as ul JOIN skidos.User as u ON ul.Id = u.Id where SubscriptionExpire is null and Reached=0 AND Date >= CURDATE() -  interval %s day AND Date < CURDATE()'''%n
    sqlCursor = connection.cursor()
    sqlCursor.execute(sqlQuery)
    FreeUserData = pd.read_sql(sqlQuery,connection)
    print(sqlQuery)
    return FreeUserData 




