from whoosh.index import open_dir

from whoosh.qparser import QueryParser

ix = open_dir("schema")

with ix.searcher() as searcher:
   
     query = QueryParser("content", ix.schema).parse("Search")
     results = searcher.search(query,)
     
     for r in results:
        #  print(results.count)
         print (r['title'], r.score)
         # Was this results object created with terms=True?
         if results.has_matched_terms():
            # What terms matched in the results?
            print(results.matched_terms()["title"])
         
 # What terms matched in each hit?
     print ("matched terms")
    #  for hit in results:
    #     print(hit) 
