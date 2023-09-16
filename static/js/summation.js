 // XL Size
 const wXLInput = document.getElementById('wXL');
 const wXLPriceInput = document.getElementById('wXLprice');
 const wXLQuantityElement = document.getElementById('wXLquantity');
 const resultXLElement = document.getElementById('wXLtotalPrice');

 wXLInput.addEventListener('input', calculateXL);
 wXLPriceInput.addEventListener('input', calculateXL);

 // M Size
 const wMInput = document.getElementById('wM');
 const wMPriceInput = document.getElementById('wMprice');
 const wMQuantityElement = document.getElementById('wMquantity');
 const wMTotalPriceElement = document.getElementById('wMtotalPrice');

 wMInput.addEventListener('input', calculateM);
 wMPriceInput.addEventListener('input', calculateM);

 // S Size
 const wSInput = document.getElementById('wS');
 const wSPriceInput = document.getElementById('wSprice');
 const wSQuantityElement = document.getElementById('wSquantity');
 const wSTotalPriceElement = document.getElementById('wStotalPrice');

 wSInput.addEventListener('input', calculateS);
 wSPriceInput.addEventListener('input', calculateS);

 // Function to calculate and display the result for XL Size
 function calculateXL() {
   const wXLValue = parseFloat(wXLInput.value) || 0;
   const wXLPriceValue = parseFloat(wXLPriceInput.value) || 0;
   const wXLTotalPrice = wXLValue * wXLPriceValue;
   
   wXLQuantityElement.textContent = wXLValue;
   resultXLElement.textContent = wXLTotalPrice;
   calculateTotal();
 }

 // Function to calculate and display the result for M Size
 function calculateM() {
   const wMValue = parseFloat(wMInput.value) || 0;
   const wMPriceValue = parseFloat(wMPriceInput.value) || 0;
   const wMTotalPrice = wMValue * wMPriceValue;
   
   wMQuantityElement.textContent = wMValue;
   wMTotalPriceElement.textContent = wMTotalPrice;
   calculateTotal();
 }

 // Function to calculate and display the result for S Size
 function calculateS() {
   const wSValue = parseFloat(wSInput.value) || 0;
   const wSPriceValue = parseFloat(wSPriceInput.value) || 0;
   const wSTotalPrice = wSValue * wSPriceValue;
   
   wSQuantityElement.textContent = wSValue;
   wSTotalPriceElement.textContent = wSTotalPrice;
   calculateTotal();
 }

 // Function to calculate the total price
 function calculateTotal() {
   const totalXL = parseFloat(resultXLElement.textContent) || 0;
   const totalM = parseFloat(wMTotalPriceElement.textContent) || 0;
   const totalS = parseFloat(wSTotalPriceElement.textContent) || 0;

   const totalPrice = totalXL + totalM + totalS;
   document.getElementById('totalPrice').textContent = totalPrice;
 }