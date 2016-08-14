$(function(){

	$("#12236").click(function(){
		id = $("#12236").text();
		$("#descripcion-sospechoso").css("display","block");
		$("#descripcion-sospechoso2").css("display","none");
		$("#descripcion-sospechoso3").css("display","none");
		$("#descripcion-sospechoso4").css("display","none");

		wSospechoso(id);
	});
	$("#18472").click(function(){
		id = $("#18472").text();
		$("#descripcion-sospechoso").css("display","none");
		$("#descripcion-sospechoso2").css("display","block");
		$("#descripcion-sospechoso3").css("display","none");
		$("#descripcion-sospechoso4").css("display","none");
		wSospechoso(id);
	});
	$("#16958").click(function(){
		id = $("#16958").text();
		$("#descripcion-sospechoso").css("display","none");
		$("#descripcion-sospechoso2").css("display","none");
		$("#descripcion-sospechoso3").css("display","block");
		$("#descripcion-sospechoso4").css("display","none");
		wSospechoso(id);
	});
	$("#05483").click(function(){
		id = $("#05483").text();
		$("#descripcion-sospechoso").css("display","none");
		$("#descripcion-sospechoso2").css("display","none");
		$("#descripcion-sospechoso3").css("display","none");
		$("#descripcion-sospechoso4").css("display","block");
		wSospechoso(id);
	});

});

function wSospechoso(id)
{
    if(id == "12236")
    {
    	$.ajax({
    	type:"POST",
    	url:"insertar_sospechoso.php",
    	data:{"id_sospechoso":id},
    	success:function(data){
    		$("#descripcion-sospechoso").html(data);
    	}
    });
    }
    if(id == "18472")
    {
    	$.ajax({
    	type:"POST",
    	url:"insertar_sospechoso.php",
    	data:{"id_sospechoso":id},
    	success:function(data){
    		$("#descripcion-sospechoso2").html(data);
    	}
    });
    }
    if(id == "16958")
    {
    	$.ajax({
    	type:"POST",
    	url:"insertar_sospechoso.php",
    	data:{"id_sospechoso":id},
    	success:function(data){
    		$("#descripcion-sospechoso3").html(data);
    	}
    });
    }
    if(id == "05483")
    {
    	$.ajax({
    	type:"POST",
    	url:"insertar_sospechoso.php",
    	data:{"id_sospechoso":id},
    	success:function(data){
    		$("#descripcion-sospechoso4").html(data);
    	}
    });
    }
}