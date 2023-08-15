var agora = new Date()
var diasem = agora.getDay()

console.log(diasem)
if (diasem== 0){
    console.log('Hoje é Domingo')
}else if(diasem==1){
    console.log('Hoje é Segunda')
}else if(diasem==2){
    console.log('Hoje é terça')
}else if(diasem==3){
    console.log('Hoje é Quarta')
}else if (diasem==4){
    console.log('Hoje é quinta')
}else if(diasem==5){
    console.log('Hoje é Sexta')
}else if(diasem==6){
        console.log('Hoje é sabado')
    }
