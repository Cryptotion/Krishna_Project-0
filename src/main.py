

import fastapi
import uvicorn
import sqlite3
from fastapi import FastAPI, Body, Depends, HTTPException
from model.schema import UserLogin, userSchema, jobpost, Employe, EmpLogin, application, userupdate, jobupdate, statusupdate
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer, userjwtBearer

app = FastAPI()



@app.get("/")
async def root():
    return {"Hello: Welcome to Revhire!"}

@app.post("/job/post", dependencies=[Depends(jwtBearer())], tags=["job"])
def post_job(post: jobpost):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO jobpost(job_id, title, company, discription, skill, emp_id) VALUES (?, ?, ?, ?, ?, ?)""", 
                       (post.job_id, post.title, post.company, post.discription, post.skill, post.emp_id)
                       )

        conn.commit()
        conn.close()

        return {"message": "Job Posted successfully"}
        # return signJWT(user.email)
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Failed to post job: Integrity constraint violation")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to post job: Internal server error")
    
@app.get("/job", dependencies=[Depends(userjwtBearer()), Depends(jwtBearer())], tags=["job"])
# @app.get("/user/details")
def get_job(job_id: int ):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobpost WHERE job_id = ?", (job_id,))
        job = cursor.fetchone()
        conn.commit()
        conn.close()

        return {"Job Details": job}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="No job Found")
    
'''
@app.put("/job/UpdateJob", dependencies=[Depends(jwtBearer())], tags=["job"])
def update_user(job_id:int, job_data: jobupdate = Body(...)):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        
        cursor.execute("UPDATE jobpost SET title=?, company=?, company=?, skill=? WHERE job_id=?", 
                       (job_data.title, job_data.company, job_data.company, job_data.skill, job_id))

        conn.commit()
        conn.close()

        return {"message": "Job Details Update successfully"}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="failed to Update Job Details!!!")
''' 




@app.post("/apply", dependencies=[Depends(userjwtBearer())], tags=["Application"])
def post_job(apply: application):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO application(app_id, user_id, job_id, status, resume_link) VALUES (?, ?, ?, ?, ?)""", 
                       (apply.app_id, apply.user_id, apply.job_id, apply.status, apply.resume_link)
                       )

        conn.commit()
        conn.close()

        return {"message": " Applied successfully!"}
        # return signJWT(user.email)
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Failed to Apply: Integrity constraint violation")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to Apply: Internal server error")
    
@app.get("/apply/getStatus", dependencies=[Depends(userjwtBearer()), Depends(jwtBearer()) ], tags=["Application"])
def post_job(app_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM application WHERE app_id = ?", (app_id,), )
        status = cursor.fetchone()

        conn.commit()
        conn.close()

        return {"Status": status}
        # return signJWT(user.email)
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Not Applied: Integrity constraint violation")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Not Applied: Internal server error")



'''
@app.put("/apply/UpdateStatus", dependencies=[Depends(jwtBearer())], tags=["Application"])
def update_user(app_id:int, app_data: statusupdate = Body(...)):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        
        cursor.execute("UPDATE application SET status=? WHERE app_id=?", 
                       (app_data.status, app_id))

        conn.commit()
        conn.close()

        return {"message": "Application Status Update successfully"}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="failed to Update Application Status!!!")
'''  



@app.post("/user/signup", tags=["user"])
def create_user(user: userSchema = Body(...)):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO USER(user_id, name, email, password, role) VALUES (?, ?, ?, ?, ?)""", 
                       (user.user_id, user.name, user.email, user.password, user.role)
                       )

        conn.commit()
        conn.close()

        return {"message": "User created successfully"}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="failed to create user")
    

def check_user(data: UserLogin):
    conn = sqlite3.connect("../revhire.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM USER WHERE email = ?", (data.email,))
    user = cursor.fetchone()  # Fetch a single row
    conn.close()

    if user:  # Check if user exists
        if user[0] == data.email and user[1] == data.password:
            return True
        else:
            return False
    else:
        return False  # User not found




@app.post("/employee/signup", tags=["Employee"])
def create_emp(user: Employe = Body(...)):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO EMPLOYEER(emp_id, name, email, password, role) VALUES (?, ?, ?, ?, ?)""", 
                       (user.emp_id, user.name, user.email, user.password, user.role)
                       )

        conn.commit()
        conn.close()

        return {"message": "User created successfully"}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="failed to create user")
    
    # empl.append(emp)

def check_emp(data: EmpLogin):
    conn = sqlite3.connect("../revhire.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM EMPLOYEER WHERE email = ?", (data.email,))
    emp = cursor.fetchone()  # Fetch a single row
    conn.close()

    if emp:  # Check if user exists
        if emp[0] == data.email and emp[1] == data.password:
            return True
        else:
            return False
    else:
        return False  # User not found

@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin = Body(...)):
    if check_user(user):
        return signJWT(user.email, user.role)
    else:
        return {
            "error" : "Invalid login details!"
        }



@app.get("/user/details", dependencies=[Depends(userjwtBearer())], tags=["user"])
# @app.get("/user/details")
def get_user(user_id: int ):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        conn.commit()
        conn.close()

        return {"user": user}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="No User Found")

    
@app.post("/employee/login", tags=["Employee"])
def user_login(emp: EmpLogin = Body(...)):
    if check_emp(emp):
        return signJWT(emp.email, emp.role)
    else:
        return {
            "error" : "Invalid login details!"
        }



@app.get("/employee/details", dependencies=[Depends(jwtBearer())], tags=["Employee"])
# @app.get("/user/details")
def get_user(emp_id: int ):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMPLOYEER WHERE emp_id = ?", (emp_id,))
        emp = cursor.fetchone()
        conn.commit()
        conn.close()

        return {"EMPLOYEE": emp}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="No User Found")

'''
@app.put("/user/UpdateUser", dependencies=[Depends(userjwtBearer())], tags=["user"])
def update_user(user_id:int, user_data: userupdate = Body(...)):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        
        cursor.execute("UPDATE user SET name=?, email=?, password=? WHERE user_id=?", 
                       (user_data.name, user_data.email, user_data.password, user_id))

        conn.commit()
        conn.close()

        return {"message": "User Details Update successfully"}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="failed to Update user Details!!!")


    
@app.put("/employee/UpdateEmplloyee", dependencies=[Depends(jwtBearer())], tags=["Employee"])
def update_user(emp_id:int, emp_data: userupdate = Body(...)):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        
        cursor.execute("UPDATE EMPLOYEER SET name=?, email=?, password=? WHERE emp_id=?", 
                       (emp_data.name, emp_data.email, emp_data.password, emp_id))

        conn.commit()
        conn.close()

        return {"message": "Employee Details Update successfully"}
        # return signJWT(user.email)
    except:
        raise HTTPException(status_code=500, detail="failed to Update Employee Details!!!")


'''