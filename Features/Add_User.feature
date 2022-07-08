Feature: Connexion d'un user

  Scenario: Saisir username user et mot de passe bitanmi
    Given launch Chrome browser
    When CLiquer sur Ajouter un uster saisir username user et password bitnami
    Then open home page et cliquer sur administration du site
    And Remplir les champs et Cliquer sur le bouton Ajouter un user