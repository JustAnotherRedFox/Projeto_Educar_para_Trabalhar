let aluno_nota1 = 1 
let aluno_nota2 = 5
let aluno_nota3 = 4

Number.parseFloat(aluno_nota1)
Number.parseFloat(aluno_nota2)
Number.parseFloat(aluno_nota3)

let nota1 = aluno_nota1.toFixed(2)
let nota2 = aluno_nota2.toFixed(2)
let nota3 = aluno_nota3.toFixed(2)

let media = (nota1 + nota2 + nota3) / 3

if (media < 5) {
	console.log('reprovado')
} else if (media < 7 && media >= 5) {
	console.log('recuperacao')
} else if (media >= 7) {
	console.log('aprovado')
} else {
	console.log('[ERROR] ' + media)
}
