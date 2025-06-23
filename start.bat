@echo off
echo 🏛️  Museu do Aeroclube do Paraná
echo ================================
echo.
echo 🚀 Iniciando servidor...
echo 🌐 Acesse: http://localhost:5000
echo 📝 Admin: http://localhost:5000/admin/login
echo 👤 Login: admin / admin
echo.
echo Pressione Ctrl+C para parar o servidor
echo ================================
echo.

cd src\backend
python app.py
pause