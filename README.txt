# To fetch data using filters from api
# To get all users and create new user
http://127.0.0.1:8000/users/
# To get any perticular user(update, delete user)
http://127.0.0.1:8000/users/2/
# To filter users with username
http://127.0.0.1:8000/users/?username=vishnu
# To search user with username
http://127.0.0.1:8000/users/?search=vishnu
# To order by ascending or descending
http://127.0.0.1:8000/users/?ordering=username
http://127.0.0.1:8000/users/?ordering=-username

# for admin log in
username:admin
password:admin123