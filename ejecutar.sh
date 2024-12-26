python app.py
echo "Agregando archivos con cambios."
git add .
echo "Haciendo un commit para guardar el estado..."
git commit -m "Nuevo Comentario Aquí..."
git commit --amend
echo "Estado: "
git status
