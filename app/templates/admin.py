<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rental Mobil</title>
    <link rel="stylesheet" href="{{url_for('static',filename='style.css')}}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dosis:wght@300;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</head>
<body id="home">
    <section>
        <nav class="navbar navbar-expand-lg shadow-sm fixed-top" style="background: whitesmoke;">
            <div class="container">
                <img src="{{url_for('static',filename='logosuper.png')}}" class="navbar-brand-logo" width="100" height="100" href="#home" ></img>
                <a class="navbar-brand " style="font-family: 'Dosis',sans-serif;font-weight: 600; font-size: 25px;padding-left: 2rem;" href="#" >Admin Page</a>
                <a class="navbar-brand " style="font-family: 'Dosis',sans-serif;font-weight: 600; font-size: 25px;padding-left: 10px;" href="#" >|</a>
                <a class="navbar-brand " style="font-family: 'Dosis',sans-serif;font-weight: 600; font-size: 25px;padding-left: 10px;" href="#" >Welcome {{username}} !</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0 gap-2" style="font-family: Dosis;font-weight: 500;font-size: larger;">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#home">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{url_for('karyawan')}}">Karyawan</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{url_for('pelanggan')}}">Pelanggan</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link"  href="{{url_for('rental')}}">Rental</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link"  href="{{url_for('mobil')}}">Mobil</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="true">
                                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-users" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 7m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" /><path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /><path d="M21 21v-2a4 4 0 0 0 -3 -3.85" /></svg>
                            </a>
                            <ul class="dropdown-menu" style="background-color:rgb(245, 243, 243);">
                                <li><a class="dropdown-item" href="{{url_for('logout')}}">Logout</a></li>
        
                            </ul>
                        </li>
                        
                    </ul>
                </div>
            </div>
        </nav>
        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true" style="background-color: #ffffff; padding-top: 6rem;">
            
            <div class="carousel-inner" style="background-color: aqua;">
            <div class="carousel-item active">
                <img src="{{url_for('static', filename='super4.jpg')}}" class="d-block w-100" alt="home1">
            </div>
            <div class="carousel-item">
                <img src="{{url_for('static', filename='super2.jpg')}}" class="d-block w-100" alt="home2">
            </div>
            <div class="carousel-item">
                <img src="{{url_for('static',filename='super1.jpg')}}" class="d-block w-100" alt="interior">
            </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
            </button>
        </div>
    </section>
    <footer id="kontak" class="p-3">
        <div class="row">
            <div class="col-md-1" style="padding-left: 2rem;padding-right: 2rem;padding-top: 1rem;">
                <a href="#home"><img src="{{url_for('static',filename='logosuper.png')}}" alt="footer-logo" width="90" height="90"></a>
            </div>
            <div class="col-md-4 text-start " style="padding-left: 4rem;">
                <div class="row">
                    <h5 class="text-white">Kontak</h5>
                    <ul>
                        <li class="text-white">WhatsApp : +62 812-2560-4346</li>
                    </ul>
                </div>
            </div>

        </div>
    </footer>










    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
