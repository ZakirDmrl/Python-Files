html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blabla Clothes</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css" integrity="sha512-SzlrxWUlpfuzQ+pcUCosxcglQRNAq/DZjVsC0lE40xsADsfeQoEypE+enwcOiGjk/bSuGGKHEyjSoQ1zVisanQ=="
            crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
    <header>
        <div class="nav-container">
            <div class="logo">
                <a href="index.html"><img src="image/logo.png"></a>
            </div>
            <div class="hamburger">
                <div class="line"></div>
                <div class="line"></div>
                <div class="line"></div>
            </div>
            <nav class="nav-bar">
                <ul>
                    <li ><a href="#" class="active">Blabla</a></li>
                    <li ><a href="#" class="catogory">Catagory</a></li>
                    <li ><a href="#" class="products">Products</a></li>
                    <li ><a href="#" class="news">News</a></li>
                
                </ul>
            </nav>
        </div>
    </header>
    
    <div class="content">
        <div class="content-box">
            <h2>Get up to 45% <br> off new products</h2>
            <label>The biggest sale of the year is at<span>Blabla Clothes</span> </label>
            <a href="#">Shop Now<i class="fa-solid fa fa-arrow-right" ></i></a>
        </div>
    </div>


    <div class="categort"id="category">
        <div class="category-title">
            <h2>Blabla Clothes Category</h2>
        </div>
        <div class="catagory-box">
            <div class="box-woman-box">
                <div class="box-content.b2">
                    <h3>Most popular styles</h3>
                    <label>Woman</label>
                    <a href="#">Go here</a>
                </div>
            </div>
                <img src="image/category-img/img-1.jpeg" alt="">

            <div class="box-man-box">
                <div class="box content.b2">
                    <h3>Last Year's Trends</h3>
                    <label >Man</label>
                    <a href="#">GO here</a>
                </div>
                <img src="image/category-img/img-2.jpeg" alt="">
            </div>
            
        </div>
    </div>
    

    <div class="most-rated">
        <div class="most-rated-box">
            <div class="most-rated-title">
                <h2>ROST RATED</h2>
            </div>
        </div>

        <div class="most-rated-items">
            <div class="most-rated-item">
                <div class="most-rated-image">
                    <img src="image/products-image/img-1.jpeg" alt="">
                </div>
                <div class="most-rated-body">
                    <h4>Woman T-Shirt</h4>
                    <div class="icons">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <div class="price">
                        <label class="sale">$89.99</label>
                        <label>$49.99</label>
                    </div>
        <div class="most-rated-items">
            <div class="most-rated-item">
                <div class="most-rated-image">
                    <img src="image/products-image/img-3.jpeg" alt="">
                </div>
                <div class="most-rated-body">
                    <h4>Unisex Shoe</h4>
                    <div class="icons">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <div class="price">
                        <label class="sale">$89.99</label>
                        <label>$49.99</label>
                    </div>
        <div class="most-rated-items">
            <div class="most-rated-item">
                <div class="most-rated-image">
                    <img src="image/products-image/img-6.jpeg" alt="">
                </div>
                <div class="most-rated-body">
                    <h4>Man T-Shirt</h4>
                    <div class="icons">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <div class="price">
                        <label class="sale">$89.99</label>
                        <label>$49.99</label>
                    </div>
                    
                                           
                        
            
                </div>
            </div>
        </div>
    </div>







    <script src="script.js"></script>
</body>
</html>

"""
from bs4 import BeautifulSoup

soup =BeautifulSoup(html_doc,'html.parser')
result = soup.prettify() #Eğer html dökümanı düzgün değilse onu düzeltir.

result = soup.head.name

result = soup.body.string

result = soup.find_all('body')
result = soup.find_all('a')[1]

result = soup.div.findChildren() #dib altındaki tüm alt elemanlar gelir.
result = soup.find_all('a')
for link in result:
    print(link.get('href'))
    