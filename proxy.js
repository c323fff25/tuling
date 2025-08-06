function setProxyArr(proArr){
    for (let i = 0; i < proArr.length; i++) {
        const element = `{
            get: function(target, propKey, receiver) {
                console.log("方法:Get ", "对象:", "${proArr[i]}", "属性值:", target[propKey], "属性:", propKey, "属性类型:", typeof propKey);
                return target[propKey];
            },
            set: function(target, propKey, value, receiver) {
                console.log("方法:Set ", "对象:", "${proArr[i]}", "属性值:", target[propKey], "属性:", propKey, "属性类型:", typeof propKey);
                return Reflect.set(...arguments)
            }
        }`
        eval(`
            try {
                ${proArr[i]};
                ${proArr[i]} = new Proxy(${proArr[i]}, ${element});
            }catch(e){
                ${proArr[i]} = {};
                ${proArr[i]} = new Proxy(${proArr[i]}, ${element});
            }
        `)
    }
}

setProxyArr(['window', 'document', 'location', 'navigator'])
