mkdir -p ~/.streamlit/credentials.toml
echo "\
[server]\n\
port = $PORT\n\
enableCORS = truw\n\
geadless = true\n\
\n\
" > ~/.streamlit/config.toml