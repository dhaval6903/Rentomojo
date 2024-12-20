from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
import mysql.connector


# Create your views here.
def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="rento_db")
    return mydb

def city_dropdown():
    try:
        city = "select * from city_tb where c_status = 'Active'"
        # query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(city)
        city_data = mycursor.fetchall()
        return city_data
    except:
        print('ERROR TO FETCH DATA')
        return None
    
def get_cart_totals(username):
   
    total_quantity = 0
    total_price = 0.00

    if username is not None:
        try:
            query = "SELECT SUM(b_quantity) as total_quantity, SUM(b_total) as total_price FROM booking_tb WHERE b_status = 'Cart' AND b_duestatus = 'Active' AND u_id = %s"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(query, (username,))
            cart_data = mycursor.fetchone()
            if cart_data:
                total_quantity = cart_data[0] if cart_data[0] is not None else 0
                total_price = cart_data[1] if cart_data[1] is not None else 0.00
        except Exception as e:
            print(f"Error in get_cart_totals: {e}")
    
    return total_quantity, total_price

def uindex(request):
    try:
        city_id = request.session.get('city_id')
        username = request.session.get('userid')
        
        query = "SELECT * FROM product_tb, category_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active'"
        
        if city_id is not None:
            query += " AND product_tb.c_id = '" + str(city_id) + "'"
        
        query += " ORDER BY RAND() LIMIT 6"
        
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        product_data = mycursor.fetchall()
        
        selcat = "select * from category_tb where cat_status = 'Active'"
        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selcat)
        cat_data = mycursor.fetchall()

        self = "select * from feedback_tb where f_status = 'Active'"
        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(self)
        f_data = mycursor.fetchall()
        
        city_data = city_dropdown()
        total_quantity, total_price = get_cart_totals(username)

        alldata = {
            'cat_data':cat_data,
            'f_data':f_data,
            'city_data' :city_data,
            'product_data' :product_data,
            'total_quantity': total_quantity,
            'total_price': total_price
            
        }
        return render(request,'uindex.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')
        
def set_city(request):
    if request.method == "POST":
        city_id = int(request.POST.get('city_id'))  # Get city_id from the POST data

        if city_id:
            request.session['city_id'] = city_id 
            
        return redirect("uindex")

def uaboutus(request):
    try:
        city_data = city_dropdown()
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)

        alldata = {
            'city_data' :city_data,
            'total_quantity': total_quantity,
            'total_price': total_price
        }
        
        return render(request,'uaboutus.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucontactus(request):
    try:
        city_data = city_dropdown()
        username = request.session.get("userid")
        if request.POST:
            f_name = request.POST.get("f_name")
            f_contact = request.POST.get("f_contact")
            f_msg = request.POST.get("f_msg")

            f_status = "Deactive"
            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `feedback_tb`(`f_name`, `f_contact`, `f_msg`, `f_status`, `f_cdate`, `f_udate`) VALUES ('"+str(f_name)+"', '"+str(f_contact)+"', '"+str(f_msg)+"', '"+str(f_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ucontactus")
        else:
            city_data = city_dropdown()
            total_quantity, total_price = get_cart_totals(username)

            alldata = {
                'city_data' :city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            
            return render(request,'ucontactus.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignup(request):
    try:
        msg = ""
        city_data = city_dropdown()
        if request.POST:
            u_name = request.POST.get("u_name")
            u_contact = request.POST.get("u_contact")
            u_address = request.POST.get("u_address")
           
            u_img = request.FILES["u_img"]
            img = FileSystemStorage()
            u_img = img.save(u_img.name,u_img)

            u_password = request.POST.get("u_password")
            
            u_status = "Active"

            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_contact)+"'"
            
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
                msg = "Sorry This Contact Is Already Exists...!"
                wholedata = {
                        'msg':msg,
                        'city_data' :city_data
                    }
                return render(request,'usignup.html',wholedata)
            else:
                ins = "INSERT INTO `user_tb`(`u_name`, `u_contact`, `u_address`, `u_img`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES ('"+str(u_name)+"','"+str(u_contact)+"','"+str(u_address)+"','"+str(u_img)+"','"+str(u_password)+"','"+str(u_status)+"','"+cdate+"','"+cdate+"')"
                #query exe - run
                
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(ins)
                mydb.commit()
                return redirect("usignin")

        else:
            alldata = {
                        'msg':msg,
                        'city_data' :city_data
                    }

            return render(request,'usignup.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignin(request):
    try:
        msg = ""
        city_data = city_dropdown()
        if request.POST:
            u_username = request.POST.get("u_username")
            u_password = request.POST.get("u_password")
           
            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_username)+"' and u_password = '"+str(u_password)+"' and u_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
                request.session["uname"] = u_username
                request.session["uimg"] = udata[0][4]
                request.session["userid"] = udata[0][0]
                request.session["utime"] = str(udata[0][8])
                
                return redirect("/")           
            else:
                
                msg = " Invalid Username or Password.!" 
                

                alldata = {
                    'msg':msg,
                    'city_data' :city_data
                }

                return render(request,'usignin.html',alldata)
        else:
            
            alldata = {
                'msg':msg,
                'city_data' :city_data
            }
            return render(request,'usignin.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignout(request):
    try:
            username = request.session["userid"]
            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE `user_tb` set `u_udate` = '"+cdate+"' where u_id = '"+str(username)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()

            request.session["uname"] = None
            request.session["uimg"] = None
            request.session["userid"] = None
            request.session["utime"] = None
            request.session['city_id'] = None
            
            return redirect("usignin")
    except NameError:
        print("internal error")
    except:
        print('Error returned')
        
def uproduct(request):
    try:
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        if request.GET.get("pname") !=None:
            product_name = request.GET.get('pname')
            city_data = city_dropdown()
            city_id = request.session.get('city_id')
            params = [f"%{product_name}%"]
            query = "SELECT * FROM product_tb, category_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active' AND product_tb.p_name LIKE %s"
            
            if city_id is not None:
                query += " AND product_tb.c_id = '" + str(city_id) + "'"
            
            query += " ORDER BY p_id desc"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(query, params)
            product_data = mycursor.fetchall()
            
            alldata = {
                'product_data' :product_data,
                'city_data' :city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            
            return render(request,'uproduct.html',alldata)
            
        elif request.GET.get("sub_id") !=None:
            sub_id = request.GET.get("sub_id")
            city_data = city_dropdown()
            city_id = request.session.get('city_id')
            
            query = "SELECT * FROM product_tb, category_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active' AND subcategory_tb.sub_id = '"+str(sub_id)+"'"
            
            if city_id is not None:
                query += " AND product_tb.c_id = '" + str(city_id) + "'"
            
            query += " ORDER BY p_id desc"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(query)
            product_data = mycursor.fetchall()
            
            alldata = {
                'product_data' :product_data,
                'city_data' :city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            
            return render(request,'uproduct.html',alldata)
        else:
            city_data = city_dropdown()
            city_id = request.session.get('city_id')
            
            query = "SELECT * FROM product_tb, category_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active'"
            
            if city_id is not None:
                query += " AND product_tb.c_id = '" + str(city_id) + "'"
            
            query += " ORDER BY p_id desc"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(query)
            product_data = mycursor.fetchall()
            
            alldata = {
                'product_data' :product_data,
                'city_data' :city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            
            return render(request,'uproduct.html',alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned")   
        print("Error returned")   
           
def usubcategory(request):
    try:
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        if request.GET.get("cat_id") !=None:
            cat_id = request.GET.get("cat_id")
            city_data = city_dropdown()
            
            query = "SELECT * FROM subcategory_tb,category_tb WHERE subcategory_tb.cat_id = category_tb.cat_id and category_tb.cat_status = 'Active' and subcategory_tb.sub_status = 'Active' AND subcategory_tb.cat_id = '"+str(cat_id)+"' order by sub_id desc"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(query)
            subcat_data = mycursor.fetchall()
            
            alldata = {
                'subcat_data' :subcat_data,
                'city_data' :city_data,
            }
            
            return render(request,'usubcategory.html',alldata)
        else:
            city_data = city_dropdown()
            query = "SELECT * FROM subcategory_tb,category_tb WHERE subcategory_tb.cat_id = category_tb.cat_id and category_tb.cat_status = 'Active' and subcategory_tb.sub_status = 'Active' order by sub_id desc"
           
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(query)
            subcat_data = mycursor.fetchall()
            
            alldata = {
                'subcat_data' :subcat_data,
                'city_data' :city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            
            return render(request,'usubcategory.html',alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def uforgotpassword(request):
    try:
        msg = ""
        city_data = city_dropdown()
        if request.POST:
            u_username = request.POST.get("u_username")
           
            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_username)+"' and u_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
                alldata = {
                    'msg':msg,
                    'udata':udata,
                    'city_data' :city_data
                }

                return render(request,'uforgotpassword.html',alldata)
                
            else:
                msg = " Sorry This Contact Is Not Registered...!" 
     
                alldata = {
                    'msg':msg,
                    'city_data' :city_data
                }

                return render(request,'uforgotpassword.html',alldata)
        else:
            
            alldata = {
                'msg':msg,
                'city_data' :city_data
            }
            return render(request,'uforgotpassword.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')
        
def uproductdetails(request):
    try:
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        if request.POST:
            p_id = request.GET.get("p_id")
            # username = request.session["userid"]        
            b_duration = request.POST.get('durationdrop')           
            b_price = request.POST.get('hprice')           
            b_deposite = request.POST.get('hdeposite')          
            b_total = request.POST.get('hcalculate')  
            b_startdate = datetime.now().strftime("%Y-%m-%d")
            b_enddate = (datetime.now() + timedelta(days=int(b_duration) * 30)).strftime("%Y-%m-%d")
            b_duestatus = 'Active'  
            b_status = 'Cart'
            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            checkproduct = "SELECT * FROM booking_tb WHERE u_id = '"+str(username)+"' AND p_id = '"+str(p_id)+"' AND b_status = 'Cart' AND b_duestatus = 'Active'"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(checkproduct)
            check_data = mycursor.fetchall()
            
            if len(check_data) > 0:
                return HttpResponse("""
                    <script>
                        alert('Oops! This item is already in your shopping cart.');
                        window.location.href = '/ucart';
                    </script>
                """)
            else:
                insbook = "INSERT INTO booking_tb (u_id,p_id,b_quantity,b_price,b_total, b_startdate, b_enddate, b_duration, b_duestatus, b_status, b_cdate, b_udate, b_deposite) VALUES ('"+str(username)+"','"+str(p_id)+"','1','"+str(b_price)+"','"+str(b_total)+"','"+b_startdate+"','"+b_enddate+"','"+str(b_duration)+"','"+str(b_duestatus)+"','"+str(b_status)+"', '"+cdate+"','"+cdate+"','"+str(b_deposite)+"')"
    
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(insbook)
                mydb.commit()  
                return redirect("/ucart")
        else:
            p_id = request.GET.get("p_id")
            city_data = city_dropdown()
            city_id = request.session.get('city_id')
            
            if p_id:
                query = "SELECT * FROM product_tb, category_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active' AND product_tb.p_id = '"+str(p_id)+"'"
                # query = "SELECT product_tb.*, category_tb.*, subcategory_tb.*, city_tb.c_name FROM product_tb, category_tb, subcategory_tb, city_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND product_tb.c_id = city_tb.c_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active' AND product_tb.p_id = '" + str(p_id) + "'"
                
                if city_id is not None:
                    query += " AND product_tb.c_id = '" + str(city_id) + "'"
                    query += " ORDER BY p_id desc"
                    
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    mycursor.execute(query)
                    pdetails_data = mycursor.fetchall()
                
            query2 = "SELECT * FROM product_tb, category_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.sub_id = subcategory_tb.sub_id AND category_tb.cat_status = 'Active' AND subcategory_tb.sub_status = 'Active' AND product_tb.p_status = 'Active'"
            if city_id is not None:
                query2 += " AND product_tb.c_id = '" + str(city_id) + "'"
                query2 += " ORDER BY p_id limit 10"
                            
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(query2)
                allp_data = mycursor.fetchall()
                alldata = {
                        'pdetails_data' :pdetails_data,
                        'city_data' :city_data,
                        'allp_data' :allp_data,
                        'total_quantity': total_quantity,
                        'total_price': total_price
                        }
                return render(request,'uproductdetails.html',alldata)
        
            
    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 
        
def uprofile(request):
    try:
        city_data = city_dropdown()
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        if request.POST:
            #variable decleration
            # username = request.session["userid"]
            u_name = request.POST.get('u_name')
            u_contact = request.POST.get('u_contact')
            u_address = request.POST.get('u_address')
            
            if request.POST.get("u_img") !="":
                p_img = request.FILES["u_img"]
                img = FileSystemStorage()
                old_img = img.save(p_img.name,p_img) 
            else:
                old_img = request.POST.get('old_img')

            u_password = request.POST.get('u_password')
          
            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #query
            updateprofile = "update user_tb set u_name = '"+str(u_name)+"',u_address = '"+str(u_address)+"',u_img = '"+str(old_img)+"',u_password = '"+str(u_password)+"',u_udate = '"+cdate+"' where u_id = '"+str(username)+"'"
            print(updateprofile)
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updateprofile)
            mydb.commit()
            return redirect("/")
        
        else:
            username = request.session["userid"]
            selprofile = "select * from user_tb where u_id = '"+str(username)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(selprofile)
            user_data = mycursor.fetchall()
            
            alldata = {
                    'user_data' :user_data,
                    'city_data' :city_data,
                    'total_quantity': total_quantity,
                    'total_price': total_price
                    }

            return render(request,'uprofile.html',alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned")  
        
def ubooking(request):
    try:
        city_data = city_dropdown()
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        # username = request.session["userid"]
        selbooking = "SELECT * FROM booking_tb,user_tb,product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.u_id = user_tb.u_id and booking_tb.b_status != 'Cart' and booking_tb.u_id = '"+str(username)+"' order by b_id desc " 
        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selbooking)
        booking_data = mycursor.fetchall()

        alldata = {
            'booking_data':booking_data,
            'city_data':city_data,
            'total_quantity': total_quantity,
            'total_price': total_price
        }
        return render(request,'ubooking.html',alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ucart(request):
    try:
        city_data = city_dropdown()
        username = request.session.get("userid")
        if request.POST:
            b1_id = ""
            payableAmount = request.POST.get('payableAmount') 
            
            city_data = city_dropdown()
            username = request.session["userid"]
            b_shippingadd = request.POST.get('b_shippingadd')
            b_pincode = request.POST.get('b_pincode')
            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            selcart = "SELECT * FROM booking_tb, product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.b_status = 'Cart' AND booking_tb.b_duestatus = 'Active' AND booking_tb.u_id = '"+str(username)+"' ORDER BY b_id DESC"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(selcart)
            cart_data = mycursor.fetchall()
            
            if len(cart_data) > 0:
                for cartdata in cart_data:
                    b1_id = b1_id + str(cartdata[0]) + "," 
                    b_id = cartdata[0] 
                    p_id = cartdata[2] 
                    b_quantity = cartdata[5] 
                    b_price = cartdata[6] 
                    b_total = cartdata[7] 
                    b_duration = cartdata[10] 
                    b_deposite = cartdata[15]  
                    b_duestatus = 'Active'  
                    b_status = 'Pending'      
                    b_startdate = datetime.now().strftime("%Y-%m-%d")
                    b_enddate = (datetime.now() + timedelta(days=int(b_duration) * 30)).strftime("%Y-%m-%d")
                    
                    # insbook = "INSERT INTO booking_tb (u_id,p_id,b_shippingadd,b_pincode,b_quantity,b_price,b_total, b_startdate, b_enddate, b_duration, b_duestatus, b_status, b_cdate, b_udate, b_deposite) VALUES ('"+str(username)+"','"+str(p_id)+"','"+str(b_shippingadd)+"','"+str(b_pincode)+"','"+str(b_quantity)+"','"+str(b_price)+"','"+str(b_total)+"','"+b_startdate+"','"+b_enddate+"','"+str(b_duration)+"','"+str(b_duestatus)+"','"+str(b_status)+"', '"+cdate+"','"+cdate+"','"+str(b_deposite)+"')"
                    updatecart = "update booking_tb set p_id = '"+str(p_id)+"',b_shippingadd = '"+str(b_shippingadd)+"',b_pincode = '"+str(b_pincode)+"',b_price = '"+str(b_price)+"',b_total = '"+str(b_total)+"',b_startdate = '"+b_startdate+"',b_enddate = '"+b_enddate+"',b_duration = '"+str(b_duration)+"',b_duestatus = '"+str(b_duestatus)+"',b_status = '"+str(b_status)+"',b_udate = '"+cdate+"',b_deposite = '"+str(b_deposite)+"' where u_id = '"+str(username)+"' AND b_id = '"+str(b_id)+"'"
                    mycursor.execute(updatecart)
                    mydb.commit()  
                    
        
                    pay_type = 'Deposite'  
                    pay_status = 'Failed' 
                    ins_payment = "INSERT INTO payment_tb (b_id, b_type, p_amount, p_status, p_cdate) VALUES ('"+str(b_id)+"','"+str(pay_type)+"','"+str(b_deposite)+"','"+str(pay_status)+"','"+cdate+"')"
                    mycursor.execute(ins_payment)
                    mydb.commit()
            
            return redirect(f"/upayment?b_id={b1_id}&payableAmount={payableAmount}&page=Deposite")
            
        elif request.GET.get("b_del") != None:
            b_del = request.GET.get("b_del")
            Delbook = "DELETE from `booking_tb` where booking_tb.b_id = '"+str(b_del)+"'"

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(Delbook)
            mydb.commit()
            return redirect("/ucart")        
        
        elif request.GET.get("status") == "plus":
            cart_id = request.GET.get("cart_id")
            selplus = "SELECT * FROM booking_tb WHERE booking_tb.b_status = 'Cart' AND booking_tb.b_id = '"+str(cart_id)+"'"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(selplus)
            plus_data = mycursor.fetchall()

            if len(plus_data) > 0:
                for plusdata in plus_data:
                    # plusdata = plus_data[0]
                    b_quantity = int(plusdata[5]) 
                    b_price = float(plusdata[6])
                    b_total = int(plusdata[7])
                    b_duration = int(plusdata[10])
                    cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    new_quantity = b_quantity + 1
                    new_total = (b_price * b_duration) * new_quantity

                    plus = "UPDATE booking_tb SET b_quantity = '"+str(new_quantity)+"', b_total = '"+str(new_total)+"', b_udate = '"+str(cdate)+"' WHERE booking_tb.b_id = '"+str(cart_id)+"'"
                    mycursor.execute(plus)
                    mydb.commit()

                return redirect("/ucart")
            
        elif request.GET.get("status") == "minus":
            cart_id = request.GET.get("cart_id")

            selplus = "SELECT * FROM booking_tb WHERE booking_tb.b_status = 'Cart' AND booking_tb.b_id = '"+str(cart_id)+"'"
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(selplus)
            plus_data = mycursor.fetchall()

            if len(plus_data) > 0:
                for plusdata in plus_data:
                    # plusdata = plus_data[0]
                    b_quantity = int(plusdata[5]) 
                    b_price = float(plusdata[6])
                    b_total = int(plusdata[7])
                    b_duration = int(plusdata[10])
                    cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    new_quantity = b_quantity - 1
                    new_total = (b_price * b_duration) * new_quantity

                    plus = "UPDATE booking_tb SET b_quantity = '"+str(new_quantity)+"', b_total = '"+str(new_total)+"', b_udate = '"+str(cdate)+"' WHERE booking_tb.b_id = '"+str(cart_id)+"'"
                    mycursor.execute(plus)
                    mydb.commit()

                return redirect("/ucart")
        
        else:
            city_data = city_dropdown()
            username = request.session ["userid"]
            selcart = "SELECT * FROM booking_tb, product_tb WHERE booking_tb.p_id = product_tb.p_id AND booking_tb.b_status = 'Cart' AND booking_tb.b_duestatus = 'Active' AND booking_tb.u_id = '"+str(username)+"' ORDER BY b_id DESC"

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(selcart)
            cart_data = mycursor.fetchall()
            
            total_quantity, total_price = get_cart_totals(username)

            alldata = {
                'cart_data': cart_data,
                'city_data': city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            return render(request, 'ucart.html', alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned")
        
def ubills(request):
    try:
        city_data = city_dropdown()
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        # username = request.session["userid"]
        bill = "SELECT * FROM bill_tb,booking_tb WHERE bill_tb.b_id = booking_tb.b_id AND booking_tb.u_id = '"+str(username)+"'" 

        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(bill)
        bill_data = mycursor.fetchall()

        alldata = {
            'bill_data':bill_data,
            'city_data':city_data,
            'total_quantity': total_quantity,
            'total_price': total_price
        }
        return render(request,'ubills.html',alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 
          
def upayment(request):
    try:
        if request.POST:
            payableAmount = request.GET.get('payableAmount')
            bill_id = request.GET.get("bill_id")
            page = request.GET.get("page")
            b_id = request.GET.get("b_id")
            b_id_list = b_id.split(",")
            cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if page == 'Deposite':
                for bid in b_id_list:
                    up1 = "update payment_tb set p_status = 'Success', p_cdate = '"+cdate+"' where b_id	 = '"+str(bid)+"'"
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    mycursor.execute(up1)
                    mydb.commit()
                return redirect("ubooking")
            else:
                for bid in b_id_list:
                    if bid != "":
                        up1 = "insert into payment_tb(b_id,b_type,p_amount,p_status,p_cdate)value('"+str(bid)+"','"+str(page)+"','"+str(payableAmount)+"','Success', '"+cdate+"')"
                        mydb = getdb()
                        mycursor = mydb.cursor()
                        mycursor.execute(up1)
                        mydb.commit()
                
                upbill = "update bill_tb set bill_status = 'Complete', bill_udate = '"+cdate+"' where bill_id = '"+str(bill_id)+"'"
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(upbill)
                mydb.commit()
                return redirect("ubills")
        else:
            return render(request,'upayment.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')
        
def upaymentlist(request):
    try:
        username = request.session.get("userid")
        total_quantity, total_price = get_cart_totals(username)
        if request.GET.get("b_id") !=None:
            city_data = city_dropdown()
            b_id = request.GET.get("b_id")
            # username = request.session["userid"]
            singlepay = "SELECT * FROM payment_tb,booking_tb WHERE payment_tb.b_id = booking_tb.b_id and payment_tb.b_id = '"+str(b_id)+"' AND booking_tb.u_id = '"+str(username)+"'" 
    
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(singlepay)
            payment_list = mycursor.fetchall()
           
            alldata = {
                'payment_list':payment_list,
                'city_data':city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            return render(request,'upaymentlist.html',alldata)
            
        else:
            city_data = city_dropdown()
            username = request.session["userid"]
            paysel = "SELECT * FROM payment_tb,booking_tb WHERE payment_tb.b_id = booking_tb.b_id AND booking_tb.u_id = '"+str(username)+"'" 

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(paysel)
            payment_list = mycursor.fetchall()

            alldata = {
                'payment_list':payment_list,
                'city_data':city_data,
                'total_quantity': total_quantity,
                'total_price': total_price
            }
            return render(request,'upaymentlist.html',alldata)
    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

     