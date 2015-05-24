 main = do
    ss <- readFile "computistas.txt"
    let d =  bar foo 1 (lines ss)
    writeFile "data.json" (unlines d)
    return "Se Genero El Json"

bar f i (s:ss) = ((f i) s ): bar f (i+1) ss
bar _ _ []     = []

foo :: Int -> String -> String
foo i x = hack $ words x
    where hack (x:xs) = "{\n" ++
                        "    \"model\": \"compushow_app.computista\",\n" ++
                        "    \"pk\": " ++ (show i) ++ ",\n" ++
                        "    \"fields\": {\n" ++
                        "        \"carnet\": " ++ "\"" ++ (baz x) ++ "\",\n" ++
                        "        \"nombre\": " ++ "\"" ++ (unwords xs) ++ "\"\n" ++
                        "    }\n" ++
                        "},"
          hack []     = ""
          baz (a:b:c) = a:b:'-':c