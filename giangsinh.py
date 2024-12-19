<!DOCTYPE html>
<html lang="en" ng-app="thiepgiangsinh">

<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/css01.css">
    <link href="https://fonts.googleapis.com/css?family=Fredoka+One" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Nunito+Sans" rel="stylesheet">
</head>

<body ng-controller="giang_sinh_ctrl">
    <div class="container-fluid ">
        <div class="container">
            <div id="bond" class="col-xs-12 col-md-12 col-sm-12 col-lg-12 text-center">
                <img id="img-play" data-toggle="modal" data-target="#myModal" class="img img-responsive img-thumbnail" src="img/virgo.PNG">
            </div>
        </div>
        <!-- Modal -->
        <div class="row">
            <div class="col-xs-12 col-md-12 col-sm-12 col-lg-12">
                <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                    <div class="modal-dialog modal-lg" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>

                                <div class="row">
                                    <div class="form-group">
                                        <h4 class="modal-title text-success bg-success col-xs-12" id="myModalLabel">Thiệp sinh nhật -
                                            <button id="play" class="btn btn-danger btn-lg" ng-click="audio.paused ? audio.play() : audio.pause()">
                                                <i class="fa fa-play" aria-hidden="true"></i>
                                                Bài hát: học tiếng mèo kêu</button>
                                            <button id="stop" class="btn btn-success btn-sm" ng-click="audio.restart()">
                                                <i class="fa fa-stop" aria-hidden="true"></i>
                                            </button>
                                            <button id="mute" class="btn btn-primary btn-sm" ng-click='audio.muting = !audio.muting'></button>

                                        </h4>


                                    </div>
                                </div>
                            </div>
                            <div class="modal-body">
                                <h1 class="heading">
                                    <div class="containeri ">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/bordercard.png">
                                        <div class=" text-danger polaroid bg-danger">Chúc mừng sinh nhật Diệp, chúc em luôn vui vẻ, hạnh phúc và yêu đời.</div>
                                    </div>
                                </h1>
                                <div class="containeri">

                                    <div class="containeri">

                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/happybirthday_s_diep.png">
                                        <!-- <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/merry-christmas_poster02.png">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/snow.jpg">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/thiepgiangsinh.jpg">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/card.jpg">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/mrcm.jpg">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/bg.jpg">
                                        <img class="img img-responsive text-center col-xs-12 col-md-12 col-sm-12 col-lg-12" src="img/caythongnoel.jpg"> -->
                                    </div>

                                </div>

                            </div>
                            <div class="modal-footer">
                                <button id="cancel" type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
                                <!-- <button type="button" class="btn btn-primary">OK</button> -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer class="container-fluid footer navbar-fixed-bottom">
            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <h1 class="text-left heading">
                            Nhân dịp sinh nhật anh Thanh tặng Diệp tấm thiệp sinh nhật thật đẹp.
                            <button id="thiepgiangsinh" class="btn btn-md btn-success" data-toggle="modal" data-target="#myModal">
                                <i class="fa fa-tree" aria-hidden="true"></i>
                                Thiệp sinh nhật</button>
                        </h1>
                    </div>
                </div>
            </div>
        </footer>
        <script src="js/jquery.js"></script>
        <script src="js/angular.min.js"></script>
        <script src="js/bootstrap.js"></script>
        <script src="js/angular.audio.js"></script>
        <script src="js/fontawesome.min.js"></script>
        <!-- <script src="js/snowstorm-min.js"></script> -->
        <script src="js/js01.js"></script> 
    </div>
</body>

</html>
