function Show_modal(id,name,Tel){


    $('#EditFarmer').modal("show");
    $("#edit_id").val(id);
    $("#edit_name").val(name);
    $("#edit_Tel").val(Tel);
  }
  const bill_id_re = 0;
  function Show_add(bill_id){

    $.ajax({
      url: '/get_products_bill?Bill_OP='+bill_id, // Replace with your actual endpoint URL
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        // Clear existing table data
        $('#TableProductlist tbody').empty();
        var loop_cnd = 1;
        // Loop through the JSON data and add rows to the table
        $.each(data, function (index, item) {
          console.log(item);
          var row = '<tr>' +
          '<td>' + loop_cnd + '</td>' +
          '<td>' + formatDate(item.Order_Date)   + '</td>' +
          '<td>' + item.Product.Product_description + '</td>' +
          '<td>' + item.Qty + '</td>' +
          '<td>' + item.Product.Product_price + '</td>' +
          '<td>' + item.Total_price + '</td>' +
          '<td class="text-end"   style=" font-weight: 700;"><button  type="button" class="btn btn-danger" onclick=delete_product('+ item.Order_Bill_id +')><i class="fa-solid fa-trash"></i></button></td>' +
          
          
          '</tr>';
        $('#TableProductlist').append(row);
          loop_cnd = loop_cnd+1;
        });
      },
      error: function (error) {
        console.error('Error fetching data:', error);
      }
    });

    
    $('#AddExpense').modal("show");
    $("#Add_Bill_id").val(bill_id);
    bill_id_re = bill_id;
  }

 


  function formatDate(isoDateString) {
    const date = new Date(isoDateString);
    const day = date.getDate();
    const month = date.getMonth() + 1; // Add 1 because months are zero-based
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
  }



  var sum = 0;
  function Show_Bill(bill_id){
    sum = 0 ;
    $('#price_H').val(0);
    $('#cost_data').val(0);
    $('#price_T').val(0);
    $('#price_M').val(0);
    $('#price_L').val(0);
    $('#qty1').text(0);
    $('#qty2').text(0);
    $('#qty3').text(0);
    $('#qty4').text(0);
    $("#price1").text(0);
    $("#price2").text(0);
    $("#price3").text(0);
    $("#price4").text(0);
    $("#cal").trigger("click");
    $('#confirm').text("");
    $.ajax({
      url: '/get_All_bill?Bill_OP='+bill_id, // Replace with your actual endpoint URL
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        console.log(data)
        var loop_cnd = 1;
        
        $('#expenttable tbody').empty();
        $.each(data['list_expent'], function (index, item) {
          console.log(item);
          var row = '<tr>' +
          '<td>' + loop_cnd + '</td>' +
        
          '<td>' + item.Product.Product_description + '</td>' +
          '<td>' + item.Qty + '</td>' +
          '<td>' + item.Product.Product_price + '</td>' +
          '<td>' + item.Total_price + '</td>' +
          '<tr>' +

          
          
          '</tr>';
        $('#expenttable').append(row);
        sum = sum+item.Total_price;
        loop_cnd = loop_cnd+1;
          
        });
        var row = '<tr>'+
        '<td class="text-end" style="background-color: black; color: #fff;" colspan="6"> ' +
            'ทั้งหมด <span style="color: #88FE31; font-weight: 700;">'+ (loop_cnd-1) +'</span> รายการ / ยอดรวมทั้งหมด <span style="color: #88FE31; font-weight: 700;">'+sum +'</span>  บาท'+
          '</td>'+
        '</tr>'

        $('#expenttable').append(row);
        if(data['bill_status'] == true){
          var count_count= data['list_Production'][0];
          console.log(count_count['H_Price'])
          $('#price_H').val(count_count['H_Price']);
          $('#price_T').val(count_count['T_Price']);
          $('#price_M').val(count_count['M_Price']);
          $('#price_L').val(count_count['L_Price']);


          $('#qty1').text(count_count['H_Qty']);
          $('#qty2').text(count_count['T_Qty']);
          $('#qty3').text(count_count['M_Qty']);
          $('#qty4').text(count_count['L_Qty']);
          $("#cal").trigger("click");
          $('#confirm').text("จ่ายแล้ว");
        }else{
          var count_count= data['list_Production'][0];
     
          $('#qty1').text(count_count['H_Qty']);
          $('#qty2').text(count_count['T_Qty']);
          $('#qty3').text(count_count['M_Qty']);
          $('#qty4').text(count_count['L_Qty']);
        }
       


      },
      error: function (error) {
        console.error('Error fetching data:', error);
      }
    });

    
    $('#Bills').modal("show");
    $("#Confirm_Bill_id").val(bill_id);


  }

  function cal_data(){
    $('#cost_data').val(0);
    $("#price1").text( $('#qty1').text() * $("#price_H").val());
    $("#price2").text( $('#qty2').text() * $("#price_T").val());
    $("#price3").text( $('#qty3').text() * $("#price_M").val());
    $("#price4").text( $('#qty4').text() * $("#price_L").val());
    var total_p = 0;
    total_p = parseInt($("#price1").text()) + parseInt($("#price2").text())+parseInt($("#price3").text())+parseInt($("#price4").text())
    $("#totalPrice").text(total_p);
    var total = total_p-sum;
    $("#cost_data").val(total);
    $("#total_cost").text(total);
  }