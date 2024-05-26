<!DOCTYPE html>
<html>
<head>
    <title>PHP et MySQL</title>
    <meta charset="utf-8"/>
</head>
<body>
    <?php
        $serveur = "localhost"; // Correction du nom du serveur
        $login = "root";
        $pass = "root";

        try {
            $connexion = new PDO("mysql:host=$serveur;dbname=test", $login, $pass); // Correction de la chaîne de connexion PDO
            $connexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            echo "Connexion à la base de données réussie."; // Ajout d'un message de confirmation
        } catch(PDOException $e) {
            echo "Erreur de connexion : " . $e->getMessage(); // Affichage de l'erreur en cas d'échec de connexion
        }
    ?>
</body>
</html>
