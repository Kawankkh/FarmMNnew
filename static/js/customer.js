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
      url: '/get_customer_bill?Production_Bill_ID='+bill_id, // Replace with your actual endpoint URL
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        console.log(data)
        $("#cus_name").text(data['cus']);
        $("#cus_tel").text(data['tel']);
        $("#cus_date").text(formatDate(data['list_Production'][0].Production_Date));
        $("#car").text(data['list_Production'][0].Car_driver);

        if(data['list_Production'][0].Pay_status == true){
          var count_count= data['list_Production'][0];
          console.log(count_count['H_Price'])
          $('#price_H').val(count_count['H_Price_c']);
          $('#price_T').val(count_count['T_Price_c']);
          $('#price_M').val(count_count['M_Price_c']);
          $('#price_L').val(count_count['L_Price_c']);


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
          $('#confirm').text("ยังไม่ได้จ่าย");
        }
       


      },
      error: function (error) {
        console.error('Error fetching data:', error);
      }
    });

    
    $('#CustomerBills').modal("show");
    $("#Production_Bill_ID").val(bill_id);


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
  function formatDate(isoDateString) {
    const date = new Date(isoDateString);
    const day = date.getDate();
    const month = date.getMonth() + 1; // Add 1 because months are zero-based
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
  }