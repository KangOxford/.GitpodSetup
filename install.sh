echo ">>> run install.sh "
# code --install-extension ms-toolsai.jupyter
# code --install-extension ms-python.python
# code --install-extension ms-toolsai.jupyter ms-python.python
echo ">>> rm -rf ~/.vscode-server"
rm -rf ~/.vscode-server
echo ">>> code --list-extensions"
code --list-extensions
echo ">>> code --install-extension"
code --install-extension ms-toolsai.jupyter && code --install-extension ms-python.python
echo ">>> cat ~/.dotfiles.log"
cat ~/.dotfiles.log
