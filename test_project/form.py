from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, SelectField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class Login(FlaskForm):
    user_name = StringField("",validators=[DataRequired()],render_kw={"placeholder": "Tên Tài Khoản"})
    user_password = PasswordField("",validators=[DataRequired()],render_kw={"placeholder": "Mật Khẩu"})
    submit = SubmitField("Đăng Nhập Ngay")

class Signup(FlaskForm):
    new_user_name = StringField("",validators=[DataRequired()],render_kw={"placeholder": "Nhập tên tài khoản"})
    new_user_email = StringField("",validators=[DataRequired()],render_kw={"placeholder": "Nhập email"})
    new_user_password = PasswordField("",validators=[DataRequired()],render_kw={"placeholder": "Nhập mật khẩu"})
    confirmed_password = PasswordField("",validators=[DataRequired()],render_kw={"placeholder": "Nhập lại mật khẩu"}) 
    
    submit = SubmitField("Đăng Kí Ngay")

class Forget_PassWord(FlaskForm):
    user_name = StringField("",validators=[DataRequired()],render_kw={"placeholder": "Tên truy cập"})
    user_email = StringField("",validators=[DataRequired()],render_kw={"placeholder": "Email hoặc số điện thoại"})
    new_user_password = PasswordField("",validators=[DataRequired()],render_kw={"placeholder": "Nhập mật khẩu mới"})
    confirmed_password = PasswordField("",validators=[DataRequired()],render_kw={"placeholder": "Nhập lại mật khẩu "}) 
    
    submit = SubmitField("Hoàn Thành")


