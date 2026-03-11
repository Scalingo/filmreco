"""
Script d'initialisation de la base de données vectorielle
"""

from src.database.vector_store import vector_store_manager


def setup_db():
    """Initialise la base de données avec les données d'exemple"""
    print("Démarrage de l'initialisation de la base de données...")
    vector_store_manager.setup_database()
    print("Initialisation terminée avec succès!")


if __name__ == "__main__":
    setup_db()
