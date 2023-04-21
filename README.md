# Brainathon

A django based project that compares Id_card and selfie & provides the id_card details.

Steps to run:

1. Download repository
2. Create your virtualenv based on your operating system
3. import the packages from `requirement.txt`
4. Setup your MySql database and make the necessary change on your settings.py file
5. Run `python manage.py makemigrations` & `python manage.py migrate`
6. `python manage.py createsuperuser`
7. Run `python manage.py runserver`
8. Then you can see webpage in that you need to click create dataset
9. It will creates 30 selfie of user and store into "ml/datset" folder
10. Now you need to upload your pan card image through this url = "localhost:port/fetch/"
11. When you click upload it will compare the images and so the message will diplayed if id_card image and selfie image are same so it shows "The both images are same" other wise not.
12. Now you can see the id_detail if both images are same and face_recognize succesfully in this url= "localhost:port/image-data/"
13. Note you need to change port number according your server
14. Enjoy
