        $(function(){
          $("#myTable").tablesorter({widgets: ['zebra']});
        });
		
    function ShowHideDiv() {	
		var dept = ["all", "Aerospace Engineering","Applied Mathematics","Architectural Engineering","Chemical Engineering","Biological Engineering","Civil Engineering","Computer Science","Electrical Engineering","Electrical and Computer Engineering","Engineering Physics","Environmental Engineering","Mechanical Engineering","Technology Arts and Media"];
		var selectedOption = document.getElementById("selectlist").value;
		for (var i = 0; i < 14; i++) {
			if (selectedOption == dept[i]) {
				var vip = document.getElementById(dept[i]);
				vip.style.display = "block" ;
			} else {
			try {
				var vip = document.getElementById(dept[i]);
				vip.style.display = "none" ;
				} catch (error){
				}
			}
		}
		
    }