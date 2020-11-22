from typing import List, Set,Mapping
from nltk.tokenize import word_tokenize
from util.time import CheckTime
from query.ranking_models import RankingModel,VectorRankingModel, IndexPreComputedVals
from index.structure import Index, TermOccurrence
from index.indexer import Cleaner

class QueryRunner:
	def __init__(self,ranking_model:RankingModel,index:Index, cleaner:Cleaner):
		self.ranking_model = ranking_model
		self.index = index
		self.cleaner = cleaner


	def get_relevance_per_query(self) -> Mapping[str,Set[int]]:
		"""
		Adiciona a lista de documentos relevantes para um determinada query (os documentos relevantes foram
		fornecidos no ".dat" correspondente. Por ex, belo_horizonte.dat possui os documentos relevantes da consulta "Belo Horizonte"

		"""
		dic_relevance_docs = {}
		for arquiv in ["belo_horizonte","irlanda","sao_paulo"]:
			with open(f"relevant_docs/{arquiv}.dat") as arq:
				dic_relevance_docs[arquiv] = set(arq.readline().split(","))
		return dic_relevance_docs

	def count_topn_relevant(self,n,respostas:List[int],doc_relevantes:Set[int]) -> int:
		"""
		Calcula a quantidade de documentos relevantes na top n posições da lista lstResposta que é a resposta a uma consulta
		Considere que respostas já é a lista de respostas ordenadas por um método de processamento de consulta (BM25, Modelo vetorial).
		Os documentos relevantes estão no parametro docRelevantes
		"""
		#print(f"Respostas: {respostas} doc_relevantes: {doc_relevantes}")
		relevance_count = 0
        

		return relevance_count

	def get_query_term_occurence(self, query:str) -> Mapping[str,TermOccurrence]:
		"""
			Preprocesse a consulta da mesma forma que foi preprocessado o texto do documento (use a classe Cleaner para isso).
			E transforme a consulta em um dicionario em que a chave é o termo que ocorreu
			e o valor é uma instancia da classe TermOccurrence (feita no trabalho prático passado).
			Coloque o docId como None.
			Caso o termo nao exista no indic, ele será desconsiderado.
		"""
		#print(self.index)
		map_term_occur = {}



		return map_term_occur

	def get_occurrence_list_per_term(self, terms:List) -> Mapping[str, List[TermOccurrence]]:
		"""
			Retorna dicionario a lista de ocorrencia no indice de cada termo passado como parametro.
			Caso o termo nao exista, este termo possuirá uma lista vazia
		"""



		return dic_terms
	def get_docs_term(self, query:str) -> List[int]:
		"""
			A partir do indice, retorna a lista de ids de documentos desta consulta
			usando o modelo especificado pelo atributo ranking_model
		"""
		#Obtenha, para cada termo da consulta, sua ocorrencia por meio do método get_query_term_occurence
		dic_query_occur = None

		#obtenha a lista de ocorrencia dos termos da consulta
		dic_occur_per_term_query = None


		#utilize o ranking_model para retornar o documentos ordenados considrando dic_query_occur e dic_occur_per_term_query
		return None

	@staticmethod
	def runQuery(query:str, indice:Index, indice_pre_computado: , map_relevantes):
		time_checker = CheckTime()

		#PEça para usuario selecionar entre Booleano ou modelo vetorial para intanciar o QueryRunner
		#apropriadamente. NO caso do booleano, vc deve pedir ao usuario se será um "and" ou "or" entre os termos.
		#abaixo, existem exemplos fixos.
		qr = QueryRunner(indice, VectorRankingModel(indice_pre_computado))
		time_checker.print_delta("Query Creation")


		#Utilize o método get_docs_term para obter a lista de documentos que responde esta consulta
		resposta = None
		time_checker.print_delta("anwered with {len(respostas)} docs")

		#nesse if, vc irá verificar se o termo possui documentos relevantes associados a ele
		#se possuir, vc deverá calcular a Precisao e revocação nos top 5, 10, 20, 50.
		#O for que fiz abaixo é só uma sugestao e o metododo countTopNRelevants podera auxiliar no calculo da revocacao e precisao
		if(True):
			arr_top = [5,10,20,50]
			revocacao = 0
			precisao = 0
			for n in arr_top:
				revocacao = 0#substitua aqui pelo calculo da revocacao topN
				precisao = 0#substitua aqui pelo calculo da revocacao topN
				print("Precisao @{n}: {precisao}")
				print("Recall @{n}: {revocacao}")

		#imprima aas top 10 respostas

	@staticmethod
	def main():
		#leia o indice (base da dados fornecida)
		index = None

		#Checagem se existe um documento (apenas para teste, deveria existir)
		print(f"Existe o doc? index.hasDocId(105047)")

		#Instancie o IndicePreCompModelo para pr ecomputar os valores necessarios para a query
		print("Precomputando valores atraves do indice...");
		check_time = CheckTime()
        



		check_time.print_delta("Precomputou valores")

		#encontra os docs relevantes
		map_relevance = None
		
		print("Fazendo query...")
		#aquui, peça para o usuário uma query (voce pode deixar isso num while ou fazer um interface grafica se estiver bastante animado ;)
		query = "São Paulo";
		runQuery(query,idx, idxPreCom,mapRelevances);
