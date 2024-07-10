document.getElementById("order_create").onclick = function PayPageSender() {
    window.location.href = "http://127.0.0.1:8000/pay/";
};

document.getElementById("payment-submit").onclick = function SuccessPayPageSender() {
    window.location.href = "http://127.0.0.1:8000/payment_success/";
};

document.getElementById("addToBasket").onclick = function productAdderToBasket() {
    
}