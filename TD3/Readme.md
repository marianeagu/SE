####  L'application de chat que j'ai implemente sera plus comme une salle de discussion. Cela signifie donc que, plusieurs utilisateurs peuvent se connecter au serveur de discussion et envoyer leurs messages. Chaque message est diffusé à chaque utilisateur de chat connecté.


##### Exécutez le serveur dans un terminal:
   $ python time_server.py 
   Chat server started on port 6666


##### Exécutez le client à partir de plusieurs terminaux:
   $ python time_client.py localhost 6666
   Connected to remote host. Start sending messages
   <You> message
   <You> text message
   <('127.0.0.1', 55719)> hello
   <You>

##### un autre terminal:
   <You> [127.0.0.1:57339] entered room
   <('127.0.0.1', 57339)> message
   <('127.0.0.1', 57339)> text message
   <You> hello

   
