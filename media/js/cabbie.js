CABBIE = {};
jQuery(document).ready(function ($) {
	CABBIE.driver = {
		/*
		init: function(csrf_token, add_item_url) {
			this.csrf_token = csrf_token;
			this.add_item_url = add_item_url;
		}, 
		incrementItem: function(sname,item_id){
			$.ajax({
				url:"/increment"+"/"+sname+"/"+item_id,
				type:"GET",
				//data:{item_id:item_id},
				success:function(request){
					//$("#table").reload("/"+sname+"/cart");
					location.reload();
				},
				error:function (xhr, textStatus, thrownError){
			        alert("error doing something");
			    }
			});
		},
		addItem: function(sname,item_id) {
			$.ajax({
			    url: "/"+sname+"/"+item_id,
			    type: "GET",
			    //data: {id_product: id_product, quantity: quantity},
			    success:function(response){},
			    complete:function(){},
			    error:function (xhr, textStatus, thrownError){
			        alert("error doing something");
			    }
			});
		},*/
		deleteItem: function(nid){
			$.ajax({
				url:"/cabbie/delete/"+nid,
				type:"GET",
				//data:{item_id:item_id},
				success:function(request){
					//$("#table").reload("/"+sname+"/cart");
					location.reload();
				},
				error:function (xhr, textStatus, thrownError){
			        alert("error doing something");
			    }
			});
		},
	};
} );