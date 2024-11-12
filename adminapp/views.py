from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage
from dateutil.relativedelta import relativedelta

# Create your views here.
def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="rento_db")
    return mydb


def index(request):
    try:
        pbooking = "SELECT count(b_id) FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Pending' and booking_tb.b_duestatus = 'Active'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(pbooking)
        pbookingcount = mycursor.fetchall()

        Combooking = "SELECT count(b_id) FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Complete' and booking_tb.b_duestatus = 'Active'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(Combooking)
        completecount = mycursor.fetchall()

        Canbooking = "SELECT count(b_id) FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Cancel' and booking_tb.b_duestatus = 'Active'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(Canbooking)
        cancelcount = mycursor.fetchall()

        payment = "SELECT count(pay_id) FROM payment_tb,booking_tb WHERE payment_tb.b_id = booking_tb.b_id" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(payment)
        paymentcount = mycursor.fetchall()

        cat = "select count(cat_id) from category_tb" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(cat)
        catcount = mycursor.fetchall()
 
        subcategory = "select count(sub_id) from subcategory_tb,category_tb where subcategory_tb.cat_id = category_tb.cat_id" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(subcategory)
        subcount = mycursor.fetchall()
        
        user = "select count(u_id) from user_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(user)
        usercount = mycursor.fetchall()

        feedback = "select count(f_id) from feedback_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(feedback)
        feedbackcount = mycursor.fetchall()

        city = "select count(c_id) from city_tb" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(city)
        citycount = mycursor.fetchall()

        product = "select count(p_id) from product_tb,category_tb,subcategory_tb,city_tb where product_tb.cat_id = category_tb.cat_id and product_tb.c_id = city_tb.c_id and  product_tb.sub_id = subcategory_tb.sub_id" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(product)
        productcount = mycursor.fetchall()

        alldata = {
            'pbookingcount': pbookingcount,
            'completecount' : completecount,
            'cancelcount' : cancelcount,
            'paymentcount' : paymentcount,
            'catcount' : catcount,
            'subcount' : subcount,
            'usercount' : usercount,
            'feedbackcount' : feedbackcount,
            'citycount' : citycount,
            'productcount' : productcount
        }
    
        return render(request,'index.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def category(request):
    try:
        if request.POST:
            cat_name = request.POST.get("cat_name")
           
            cat_img = request.FILES["cat_image"]
            img = FileSystemStorage()
            cat_image = img.save(cat_img.name,cat_img)
            
            cat_status = request.POST.get("cat_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `category_tb`(`cat_name`, `cat_img`, `cat_status`, `cat_cdate`, `cat_udate`) VALUES ('"+str(cat_name)+"','"+str(cat_image)+"','"+str(cat_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("category")
            
        elif request.GET.get("cat_del") !=None:
            #variable decleration
            cat_del = request.GET.get("cat_del")

            #insert query

            ins = "DELETE from `category_tb` where cat_id = '"+str(cat_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("category")

        else:    
            selcat = "select * from category_tb order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            return render(request,'category.html',{'cat_data': cat_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def categoryedit(request):
    try:
       if request.POST:
           #variable decleration
           cat_edt = request.GET.get("cat_edt")
           cat_name = request.POST.get("cat_name")
           
           if request.POST.get("cat_img") !="":
               cat_img = request.FILES["cat_img"]
               img = FileSystemStorage()
               old_img = img.save(cat_img.name,cat_img)

           else:
               old_img = request.POST.get("old_img")

           cat_status = request.POST.get("cat_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `category_tb` set `cat_name` = '"+str(cat_name)+"', `cat_img` = '"+str(old_img)+"', `cat_status` = '"+str(cat_status)+"', `cat_udate` = '"+cdate+"' where cat_id = '"+str(cat_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("category")

       else:
            
            cat_edt = request.GET.get("cat_edt")
            selcat = "select * from category_tb where cat_id = '"+str(cat_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall() 
            return render(request,'category-edit.html',{'cat_data': cat_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def subcategory(request):
    try:
        if request.POST:
            
            cat_id = request.POST.get("cat_id")
            sub_name = request.POST.get("sub_name")
           
            sub_img = request.FILES["sub_img"]
            img = FileSystemStorage()
            sub_image = img.save(sub_img.name,sub_img)
            
            sub_status = request.POST.get("sub_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `subcategory_tb`(`cat_id`,`sub_name`, `sub_img`, `sub_status`, `sub_cdate`, `sub_udate`) VALUES ('"+str(cat_id)+"','"+str(sub_name)+"','"+str(sub_image)+"','"+str(sub_status)+"','"+cdate+"','"+cdate+"')"
            print(ins)
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("subcategory")
        
        elif request.GET.get("sub_del") !=None:
            #variable decleration
            sub_del = request.GET.get("sub_del")

            #insert query

            ins = "DELETE from `subcategory_tb` where sub_id = '"+str(sub_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("subcategory")

        else:    
            selsubcategory = "select * from subcategory_tb,category_tb where subcategory_tb.cat_id = category_tb.cat_id order by sub_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsubcategory)
            sub_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active' order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            alldata = {
                'sub_data' : sub_data,
                'cat_data' : cat_data
            }

            return render(request,'subcategory.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def subcategoryedit(request):
    try:
       if request.POST:
           #variable decleration
           sub_edt = request.GET.get("sub_edt")
           
           cat_id = request.POST.get("cat_id")
           sub_name = request.POST.get("sub_name")
           
           if request.POST.get("sub_img") !="":
               sub_img = request.FILES["sub_img"]
               img = FileSystemStorage()
               old_img = img.save(sub_img.name,sub_img)

           else:
               old_img = request.POST.get("old_img")

           sub_status = request.POST.get("sub_status")
           subdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `subcategory_tb` SET `cat_id`='"+str(cat_id)+"',`sub_name`='"+str(sub_name)+"',`sub_img`='"+str(old_img)+"',`sub_status`='"+str(sub_status)+"',`sub_udate`= '"+subdate+"' WHERE sub_id = '"+str(sub_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("subcategory")

       else:  
            
            sub_edt = request.GET.get("sub_edt")

            selsubcategory = "select * from subcategory_tb where sub_id = '"+str(sub_edt)+"'" 
            print(selsubcategory)
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsubcategory)
            sub_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            alldata = {
                'sub_data' : sub_data,
                'cat_data' : cat_data
            }

            return render(request,'subcategory-edit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def city(request):
    try:
        if request.POST:
            c_name = request.POST.get("c_name")
           
            
            c_status = request.POST.get("c_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `city_tb`(`c_name`, `c_status`, `c_cdate`, `c_udate`) VALUES ('"+str(c_name)+"','"+str(c_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("city")
            
        elif request.GET.get("c_del") !=None:
            #variable decleration
            c_del = request.GET.get("c_del")

            #insert query

            ins = "DELETE from `city_tb` where c_id = '"+str(c_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("city")

        else:    
            selcat = "select * from city_tb order by c_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall()

            return render(request,'city.html',{'c_data': c_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def cityedit(request):
    try:
       if request.POST:
           #variable decleration
           c_edt = request.GET.get("c_edt")
           c_name = request.POST.get("c_name")
           
           
           c_status = request.POST.get("c_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `city_tb` set `c_name` = '"+str(c_name)+"', `c_status` = '"+str(c_status)+"', `c_udate` = '"+cdate+"' where c_id = '"+str(c_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("city")

       else:
            
            c_edt = request.GET.get("c_edt")
            selcat = "select * from city_tb where c_id = '"+str(c_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall() 
            return render(request,'city-edit.html',{'c_data': c_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def login(request):
    try:
        msg = ""
        if request.POST:
           #variable decleration
           a_username = request.POST.get("a_username")
           a_password = request.POST.get("a_password")
           
           #insert query
           sel = "select * from login_tb where `l_username` = '"+str(a_username)+"' and l_password = '"+str(a_password)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(sel)
           udata = mycursor.fetchall()

           if len(udata) > 0:
               request.session["name"] = a_username
               request.session["img"] = udata[0][3]
               request.session["time"] = str(udata[0][4])
        
               return redirect("index")           
           else:
               msg = " Invalid Username or Password.!" 
               return render(request,'login.html',{'msg':msg})          
        else:
            return render(request,'login.html',{'msg':msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def logout(request):
    try:
        
            #variable decleration
            username = request.session["name"]
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query

            ins = "UPDATE `login_tb` set `l_lastseen` = '"+cdate+"' where l_username = '"+str(username)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()

            request.session["name"] = None
            request.session["img"] = None
            request.session["time"] = None

            return redirect("login")
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def product(request):
    try:
        if request.POST:

            cat_id = request.POST.get("cat_id")
            c_id = request.POST.get("c_id")
            sub_id = request.POST.get("sub_id")
            p_name = request.POST.get("p_name")
            
            p_img1 = request.FILES["p_img1"]
            img1 = FileSystemStorage()
            p_image1 = img1.save(p_img1.name,p_img1)

            p_img2 = request.FILES["p_img2"]
            img2 = FileSystemStorage()
            p_image2 = img2.save(p_img2.name,p_img2)


            p_img3 = request.FILES["p_img3"]
            img3 = FileSystemStorage()
            p_image3 = img3.save(p_img3.name,p_img3)
            
            p_detail = request.POST.get("p_detail")
            p_size = request.POST.get("p_size")
            p_color = request.POST.get("p_color")
            p_material = request.POST.get("p_material")
            p_mrp = request.POST.get("p_mrp")
            p_price = request.POST.get("p_price")
            p_deposite = request.POST.get("p_deposite")           
            p_status = request.POST.get("p_status")
            pdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `product_tb`(`cat_id`, `sub_id`,`c_id`, `p_name`,`p_details`, `p_img1`, `p_img2`,`p_img3`, `p_size`, `p_color`, `p_material`,`p_mrp`,`p_price`, `p_status`, `p_cdate`, `p_udate`,`p_deposite`) VALUES ('"+str(cat_id)+"','"+str(sub_id)+"','"+str(c_id)+"','"+str(p_name)+"','"+str(p_detail)+"','"+str(p_image1)+"','"+str(p_image2)+"','"+str(p_image3)+"','"+str(p_size)+"','"+str(p_color)+"','"+str(p_material)+"','"+str(p_mrp)+"','"+str(p_price)+"','"+str(p_status)+"','"+pdate+"','"+pdate+"','"+str(p_deposite)+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("product")

        elif request.GET.get("p_del") !=None:
            #variable decleration
            p_del = request.GET.get("p_del")

            #insert query

            ins = "DELETE from `product_tb` where p_id = '"+str(p_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("product")

        elif request.GET.get("p_status") !=None:
            #variable decleration
            p_status = request.GET.get("p_status")
            status = request.GET.get("status")
            if status == 'Active':
                p_status = 'Deactive'
            else:
                p_status = 'Active'
            #insert query

            upd = "update product_tb set  p_status = '"+str(p_status)+"' where  p_id = '"+str(p_status)+"'"
             #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("product")

        else:    
            selproduct = "select * from product_tb,category_tb,subcategory_tb,city_tb where product_tb.cat_id = category_tb.cat_id and product_tb.c_id = city_tb.c_id and  product_tb.sub_id = subcategory_tb.sub_id order by product_tb.p_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selproduct)
            p_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            selsub = "select * from subcategory_tb where sub_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsub)
            sub_data = mycursor.fetchall()

            selcity = "select * from city_tb where c_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcity)
            c_data = mycursor.fetchall()

            alldata = {
                'p_data': p_data,
                'cat_data' : cat_data,
                'sub_data' : sub_data,
                'c_data':c_data
            } 
            return render(request,'product.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def productedit(request):
    try:
        if request.POST:
            
            p_edt = request.GET.get("p_edt")
            c_id = request.POST.get("c_id")
            cat_id = request.POST.get("cat_id")
            sub_id = request.POST.get("sub_id")
            p_name = request.POST.get("p_name")
            
            if request.POST.get("p_img1") !="":
                p_img1 = request.FILES["p_img1"]
                img1 = FileSystemStorage()
                old_img1 = img1.save(p_img1.name,p_img1)
            else:
               old_img1 = request.POST.get("old_img1")

            if request.POST.get("p_img2") !="":
                p_img2 = request.FILES["p_img2"]
                img2 = FileSystemStorage()
                old_img2 = img2.save(p_img2.name,p_img2)
            else:
               old_img2 = request.POST.get("old_img2")

            if request.POST.get("p_img3") !="":
                p_img3 = request.FILES["p_img3"]
                img3 = FileSystemStorage()
                old_img3 = img3.save(p_img3.name,p_img3)
            else:
               old_img3 = request.POST.get("old_img3")
            
            p_detail = request.POST.get("p_detail")
            p_size = request.POST.get("p_size")
            p_color = request.POST.get("p_color")
            p_material = request.POST.get("p_material")
            p_mrp = request.POST.get("p_mrp")
            p_price = request.POST.get("p_price")
            p_deposite = request.POST.get("p_deposite")              
            p_status = request.POST.get("p_status")
            pdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "UPDATE `product_tb` SET `c_id`='"+str(c_id)+"',`cat_id`='"+str(cat_id)+"',`sub_id`='"+str(sub_id)+"',`p_name`='"+str(p_name)+"',`p_img1`='"+str(old_img1)+"',`p_img2`='"+str(old_img2)+"',`p_img2`='"+str(old_img3)+"',`p_details`='"+str(p_detail)+"',`p_size`='"+str(p_size)+"',`p_color`='"+str(p_color)+"',`p_material`='"+str(p_material)+"',`p_mrp`='"+str(p_mrp)+"',`p_price`='"+str(p_price)+"',`p_status`='"+str(p_status)+"',`p_udate`= '"+pdate+"',`p_deposite`='"+str(p_deposite)+"' WHERE p_id = '"+str(p_edt)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("product")

        else:
            p_edt = request.GET.get("p_edt")

            selproduct = "select * from product_tb where p_id = '"+str(p_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selproduct)
            p_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            selsub = "select * from subcategory_tb where sub_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsub)
            sub_data = mycursor.fetchall()

            selcity = "select * from city_tb where c_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcity)
            c_data = mycursor.fetchall()

            alldata = {
                'p_data': p_data,
                'cat_data' : cat_data,
                'sub_data' : sub_data,
                'c_data' : c_data
            } 

            return render(request,'product-edit.html',alldata)

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def feedback(request):
    try:
        if request.GET.get("feedback_del") !=None:
            feedback_del = request.GET.get("feedback_del")

            #insert query

            dele = "DELETE from feedback_tb where f_id = '"+str(feedback_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dele)
            mydb.commit()
            return redirect("feedback")
            
        elif request.GET.get("feedback_status") !=None:
            #variable decleration
            feedback_status = request.GET.get("feedback_status")
            status = request.GET.get("status")
            if status == 'Active':
                f_status = 'Deactive'
            else:
                f_status = 'Active'
            #insert query

            upd = "update feedback_tb set  f_status = '"+str(f_status)+"' where  f_id = '"+str(feedback_status)+"'"
             #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("feedback")
        else:
            selfeedback = "select * from feedback_tb order by f_id desc" 
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selfeedback)
            feedback_data = mycursor.fetchall()
            return render(request,'feedback.html',{'feedback_data': feedback_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def user(request):
    try:
        if request.GET.get("user_del") !=None:
            user_del = request.GET.get("user_del")

            #insert query

            dele = "DELETE from user_tb where u_id = '"+str(user_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dele)
            mydb.commit()
            return redirect("user")

        elif request.GET.get("user_status") !=None:
            #variable decleration
            user_status = request.GET.get("user_status")
            status = request.GET.get("status")
            if status == 'Active':
                u_status = 'Deactive'
            else:
                u_status = 'Active'
            #insert query

            upd = "update user_tb set  u_status = '"+str(u_status)+"' where  u_id = '"+str(user_status)+"'"
             #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("user")
        else:
            seluser = "select * from user_tb order by u_id desc" 
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            user_data = mycursor.fetchall()
            return render(request,'user.html',{'user_data': user_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def payment(request):
    try:
        if request.GET.get("payment_del") !=None:
            payment_del = request.GET.get("payment_del")

            #insert query

            dele = "DELETE from payment_tb where pay_id = '"+str(payment_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dele)
            mydb.commit()
            return redirect("payment")

        elif request.GET.get("payment_status") !=None:
            #variable decleration
            payment_status = request.GET.get("payment_status")
            status = request.GET.get("status")

            if status == 'Success':
                status = 'Failed'
            else:
                status = 'Success'
            #insert query

            upd = "update payment_tb set  p_status = '"+str(status)+"' where  pay_id = '"+str(payment_status)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("payment")
        else:
            selpayment = "SELECT * FROM payment_tb,booking_tb WHERE payment_tb.b_id = booking_tb.b_id order by pay_id desc" 
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpayment)
            payment_data = mycursor.fetchall()
        return render(request,'payment.html',{'payment_data': payment_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')  

def pendingbooking(request):
    try:
        if request.GET.get("booking_del") !=None:
            booking_del = request.GET.get("booking_del")

            #insert query

            dele = "DELETE from booking_tb where b_id = '"+str(booking_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dele)
            mydb.commit()
            return redirect("pendingbooking")
            
        elif request.GET.get("booking_status") !=None:
            #variable decleration
            booking_status = request.GET.get("booking_status")
            status = request.GET.get("status")
            
            if status == 'Pending':
                status = 'Complete'
                
            elif status == 'Complete':
                 status = 'Cancel'

            else:
                status = 'Pending'
            #insert query

            upd = "update booking_tb set  b_status = '"+str(status)+"' where  b_id = '"+str(booking_status)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("pendingbooking")
        else:
            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Pending' and booking_tb.b_duestatus = 'Active' order by b_id desc" 
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()
            return render(request,'pendingbooking.html',{'booking_data': booking_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def completebooking(request):
    try:
        if request.GET.get("booking_del") !=None:
            booking_del = request.GET.get("booking_del")

            #insert query

            dele = "DELETE from booking_tb where b_id = '"+str(booking_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dele)
            mydb.commit()
            return redirect("completebooking")
            
        elif request.GET.get("booking_status") !=None:
            #variable decleration
            booking_status = request.GET.get("booking_status")
            status = request.GET.get("status")
            
            if status == 'Pending':
                status = 'Complete'
                
            elif status == 'Complete':
                 status = 'Cancel'

            else:
                status = 'Pending'
            #insert query

            upd = "update booking_tb set  b_status = '"+str(status)+"' where  b_id = '"+str(booking_status)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("completebooking")
        else:
            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Complete' and booking_tb.b_duestatus = 'Active' order by b_id desc" 
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()
            return render(request,'completebooking.html',{'booking_data': booking_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def cancelbooking(request):
    try:
        if request.GET.get("booking_del") !=None:
            booking_del = request.GET.get("booking_del")

            #insert query

            dele = "DELETE from booking_tb where b_id = '"+str(booking_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dele)
            mydb.commit()
            return redirect("cancelbooking")
            
        elif request.GET.get("booking_status") !=None:
            #variable decleration
            booking_status = request.GET.get("booking_status")
            status = request.GET.get("status")
            
            if status == 'Pending':
                status = 'Complete'
                
            elif status == 'Complete':
                 status = 'Cancel'

            else:
                status = 'Pending'
            #insert query

            upd = "update booking_tb set  b_status = '"+str(status)+"' where  b_id = '"+str(booking_status)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(upd)
            mydb.commit()
            return redirect("cancelbooking")
        else:
            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Cancel' and booking_tb.b_duestatus = 'Active' order by b_id desc" 
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()
            return render(request,'cancelbooking.html',{'booking_data': booking_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def userreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            u_status = request.POST.get("u_status")

            seluser = "select * from user_tb where  DATE(user_tb.u_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by u_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            user_data = mycursor.fetchall()
            return render(request,'userreport.html',{'user_data': user_data})
        else:
            return render(request,'userreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def feedbackreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date") 

            selfeedback = "select * from feedback_tb where  DATE(feedback_tb.f_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by f_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selfeedback)
            feedback_data = mycursor.fetchall()
            return render(request,'feedbackreport.html',{'feedback_data': feedback_data})
        else:
            return render(request,'feedbackreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def productsreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            
            selproducts = "select * from product_tb,category_tb,subcategory_tb,city_tb where product_tb.cat_id = category_tb.cat_id and product_tb.c_id = city_tb.c_id and  product_tb.sub_id = subcategory_tb.sub_id and DATE(product_tb.p_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by p_id desc " 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selproducts)
            products_data = mycursor.fetchall()

            
            return render(request,'productsreport.html',{'products_data': products_data})

        else:
            
            return render(request,'productsreport.html',{})
            
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def bookingreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            b_status = request.POST.get("b_status")

            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = '"+str(b_status)+"'  and DATE(booking_tb.b_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' "
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()
            return render(request,'bookingreport.html',{'booking_data': booking_data})
        else:
            return render(request,'bookingreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def generatebill(request):
    try:
        msg = ""
        if request.POST:

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # pdate = datetime.datetime.now()
            # next_date = pdate + datetime.timedelta(days=30)
            # formatted_next_date = next_date.strftime("%Y-%m-%d")
            bill_month = request.POST.get("bill_month")

            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_duestatus = 'Active' and booking_tb.b_status = 'Complete' "
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()

            if len(booking_data) > 0:
                
                for booking in booking_data:
                    booking_id = booking[0]  # Assuming booking_tb.b_id is the first field
                    booking_rent =  float(booking[7])
                    booking_date =  str(booking[8])
                    date_parts = booking_date.split("-")
                    day = date_parts[2]

                    bill_month_parts = bill_month.split("-")
                    month = bill_month_parts[0] 
                    year = bill_month_parts[1] 

                    newstartdate = f"{year}-{month}-{day}"
                    pdate = datetime.datetime.strptime(newstartdate,"%Y-%m-%d")
                    formatted_pdate = pdate.strftime("%Y-%m-%d")
                    next_date = pdate + datetime.timedelta(days=30)
                    formatted_next_date = next_date.strftime("%Y-%m-%d")
                    

                    selmonth = "SELECT DATE_FORMAT(DATE_ADD(b_startdate, INTERVAL t.n MONTH), '%m-%Y') AS month FROM booking_tb, ( SELECT @row := @row + 1 AS n FROM (SELECT 0 UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10 UNION ALL SELECT 11) a, (SELECT @row := -1) b ) t WHERE b_id = '"+str(booking_id)+"' AND DATE_ADD(b_startdate, INTERVAL t.n MONTH) < b_enddate"
                    # connection create object
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    #query execute
                    mycursor.execute(selmonth)
                    month_data = mycursor.fetchall()

                    if len(month_data) > 0:
                        for monthdata in month_data:
                            billmonthdata = monthdata[0] 
                            if billmonthdata == bill_month:

                                selbill = "SELECT * FROM bill_tb  WHERE bill_month = '"+str(billmonthdata)+"' and b_id = '"+str(booking_id)+"'"
                                # connection create object
                                mydb = getdb()
                                mycursor = mydb.cursor()
                                #query execute
                                mycursor.execute(selbill)
                                bill_data = mycursor.fetchall()
                                bill_status = "Pending"

                                if len(bill_data) == 0:
                                    
                                    #print("Hello")
                                    ins = "INSERT INTO `bill_tb`( `b_id`, `bill_startdate`, `bill_enddate`, `bill_month`, `bill_rent`, `bill_status`, `bill_cdate`, `bill_udate`) VALUES ('"+str(booking_id)+"','"+formatted_pdate+"','"+formatted_next_date+"','"+str(bill_month)+"','"+str(booking_rent)+"','"+str(bill_status)+"','"+cdate+"','"+cdate+"')"
                                   
                                    #query exe - run
                                    mydb = getdb()
                                    mycursor = mydb.cursor()
                                    mycursor.execute(ins)
                                    mydb.commit()

                return redirect("generatebill")

            else:
                selbill = "SELECT * FROM bill_tb"
                # connection create object
                mydb = getdb()
                mycursor = mydb.cursor()
                #query execute
                mycursor.execute(selbill)
                bill_data = mycursor.fetchall()
                msg = "No any Record Found.!"
                alldata = {
                    'msg' : msg,
                    'bill_data' : bill_data 
                    }
                return render(request,'generatebill.html',alldata)        

               
               
        else:
           
            selbill = "SELECT * FROM bill_tb"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbill)
            bill_data = mycursor.fetchall()
            msg = ""
            alldata = {
                'msg' : msg,
                'bill_data' : bill_data 
                }
            return render(request,'generatebill.html',alldata)

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def discontinuerent(request):
    try:
        msg = ""
        if request.POST:

            pdate = datetime.datetime.now().strftime("%Y-%m-%d")        
            

            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_duestatus = 'Active' and booking_tb.b_status = 'Complete' and booking_tb.b_enddate <= '"+pdate+"' "
            
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()
            if len(booking_data) > 0:
                for booking in booking_data:
                    booking_id = booking[0]  # Assuming booking_tb.b_id is the first field
                    update_query = "UPDATE booking_tb SET b_duestatus = 'Deactive' WHERE b_id = '"+str(booking_id)+"'"
                    mycursor.execute(update_query)
                    mydb.commit()
                
            
                return redirect("discontinuerent")
            else:
                selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Complete' and booking_tb.b_duestatus = 'Deactive'"
            
                # connection create object
                mydb = getdb()
                mycursor = mydb.cursor()
                #query execute
                mycursor.execute(selbooking)
                booking_data = mycursor.fetchall()
                msg = "No any Record Found.!"
                alldata = {
                    'msg' : msg,
                    'booking_data' : booking_data 
                    }
                return render(request,'discontinuerent.html',alldata)
        else:
            selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status = 'Complete' and booking_tb.b_duestatus = 'Deactive'"
            
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selbooking)
            booking_data = mycursor.fetchall()
            msg = ""
            alldata = {
                'msg' : msg,
                'booking_data' : booking_data 
                }
            return render(request,'discontinuerent.html',alldata)
            #return render(request,'discontinuerent.html',{'booking_data': booking_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def paymentreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
          

            selworker = "SELECT * FROM payment_tb,booking_tb WHERE payment_tb.b_id = booking_tb.b_id and DATE(payment_tb.p_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by p_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selworker)
            payment_data = mycursor.fetchall()
            return render(request,'paymentreport.html',{'payment_data': payment_data})
        else:
            return render(request,'paymentreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

