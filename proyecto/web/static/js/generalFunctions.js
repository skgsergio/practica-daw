/**
 * Created by Alex on 13/05/2015.
 */

$( document ).ready(function() {
   $("#addEquipo").click(function () {
      addEquipo($(this).data("token"));
    });
   
   $("#addCompeticion").click(function () {
      addLiga($(this).data("token"));
    });

   $("#editEquipo").click(function () {
      modifyEq($(this).data("token"));
    });

   $("#editCompeticion").click(function () {
      modifyComp($(this).data("token"));
    });

   $("#editJugador").click(function () {
        modifyJug($(this).data("token"));
    });

   $("#addJugador").click(function () {
      addJugador($(this).data("token"));
    });
   
   $(".day").click(function () {
    $('.day').removeClass('active');
    $(this).addClass('active');
    if(document.getElementById('editCompeticion')){
      jornada($(this).data("jornada"),$(this).data("competicion"),$(this).data("token"));
    }else{
       jornadaVisual($(this).data("jornada"),$(this).data("competicion"));
    }
    });

   if($('.old').length > 0){
      $('.old')[0].setAttribute("class", $('.old')[0].getAttribute("class")+" active");
   }

});


function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}