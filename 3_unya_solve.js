var p = Array(70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449);
var p2utf = p.map((value, index) => {
    return value / (index + 1);
});

//スプレット演算
var t = String.fromCharCode(...p2utf);
console.log(t);