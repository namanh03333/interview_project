from test_project import create_app, db  
from test_project.models import Product,Category
app = create_app()

with app.app_context():
    db.create_all()
    
    cat_men = Category(name="Đồ Nam")
    cat_women = Category(name="Đồ Nữ")
    cat_kid_boy = Category(name="Trẻ em Nam")
    cat_kid_girl = Category(name="Trẻ em Nữ")

    db.session.add_all([cat_men, cat_women, cat_kid_boy, cat_kid_girl])
    db.session.commit()

    
    p1 = Product(
        name="Áo Nam Tay Ngắn",
        price=199000,
        type="Áo",
        img_url="images/p1.png",
        category_id=cat_men.id
    )
    p2 = Product(
        name="Áo Len lông Cừu",
        price=499000,
        type="Áo Len",
        img_url="images/p2.png",
        category_id=cat_men.id
    )
    p3 = Product(
        name="Áo Len Gile",
        price=399000,
        type="Áo Len",
        img_url="images/p3.png",
        category_id=cat_men.id
    )
    p4 = Product(
        name="Áo Len Nam ",
        price=299000,
        type="Áo",
        img_url="images/p4.png",
        category_id=cat_men.id
    )
    p5 = Product(
        name="Áo Tay Dài Nữ",
        price=299000,
        type="Áo",
        img_url="images/p5.png",
        category_id=cat_women.id
    )
    p6 = Product(
        name="Áo Len Cổ Tím",
        price=320000,
        type="Áo Len",
        img_url="images/p6.png",
        category_id=cat_women.id
    )
    p7 = Product(
        name="Áo Len Tay Lửng Nữ",
        price=320000,
        type="Áo Len",
        img_url="images/p7.png",
        category_id=cat_women.id
    )
    p8 = Product(
        name="Áo Len Nữ",
        price=399000,
        type="Áo Len",
        img_url="images/p8.png",
        category_id=cat_women.id
    )
    p9 = Product(
        name="Áo Nam Tay Dài",
        price=199000,
        type="Áo",
        img_url="images/p9.png",
        category_id=cat_kid_boy.id
    )
    p10 = Product(
        name="Áo Nam Tay Ngắn",
        price=199000,
        type="Áo",
        img_url="images/p10.png",
        category_id=cat_kid_boy.id
    )
    p11 = Product(
        name="Áo Nữ Tay Ngắn",
        price=199000,
        type="Áo",
        img_url="images/p11.png",
        category_id=cat_kid_girl.id
    )
    p12 = Product(
        name="Áo Len Nữ Tay Dài",
        price=199000,
        type="Áo",
        img_url="images/p12.png",
        category_id=cat_kid_girl.id
    )

    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])
    db.session.commit()
