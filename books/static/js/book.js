document.addEventListener('DOMContentLoaded', function () {
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                let price = document.getElementById('price').innerHTML;
                let preCurrency = 'USD';
                let preRate = data.rates[preCurrency];
                console.log(price);
                document.getElementById('Currency').onchange = function () {
                    const currency = this.value;

                    const rate = data.rates[currency];
                    console.log(preCurrency);


                    if(currency === 'NZD' && preCurrency === 'USD') {
                        price = (price * rate).toFixed(2);
                        document.querySelector('#price').innerHTML = price.toString();
                        preCurrency = 'NZD';
                        preRate = rate;
                    } else if(currency === 'USD' && preCurrency === 'NZD') {
                        price = (price / preRate).toFixed(2);
                        document.querySelector('#price').innerHTML = price.toString();
                        preRate = rate;
                        preCurrency = 'USD';
                    }
                }
            })
            .catch(error => {
                console.log('Error', error);
            });

});