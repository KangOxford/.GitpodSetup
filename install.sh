echo ">>> install.sh Done."
# code --install-extension ms-toolsai.jupyter
# code --install-extension ms-python.python
# code --install-extension ms-toolsai.jupyter ms-python.python
code --list-extensions
code --install-extension ms-toolsai.jupyter && code --install-extension ms-python.python
cat ~/.dotfiles.log
