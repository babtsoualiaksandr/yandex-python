const maxProfit = function (prices) {
    return calculate(prices, 0);
};

function calculate(prices, index) {
    if (index >= prices.length) {
        return 0;
    }

    let maxProfix = 0;

    for (var start = index; start < prices.length; start++) {
        var localMaxProfit = 0;
        for (var i = start + 1; i < prices.length; i++) {
            if (prices[start] < prices[i]) {
                var profit =
                    calculate(prices, i + 1) + prices[i] - prices[start];
                if (profit > localMaxProfit) {
                    localMaxProfit = profit;
                }
            }
        }

        if (localMaxProfit > maxProfix) maxProfix = localMaxProfit;
    }


    prices.map((iter, inx) => {
        let localMaxProfit = 0;
        const localMax = prices.map((item, index) => {
            if (iter < item) {
                const profit =
                    calculate(prices, index + 1) + item - prices[inx];
                if (profit > localMaxProfit) {
                    localMaxProfit = profit;
                }
            }
            return localMaxProfit;
        });
        if (localMax > maxProfix) maxProfix = localMax;
        return maxProfit;
    });
}



m = maxProfit([12,34,56,34])
