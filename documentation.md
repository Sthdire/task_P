Вivide and Сonquer API

API для создания и изменения рассылок

Base url: http://127.0.0.1:5000/api

  Methods:
  
    Client:
      POST: '/add_client/phone=<yorePhone>'
        Returns:
                {
                  "phone_n": "yorePhone",
                  "timezone": ""
                }
  
      POST: '/add_client/phone=<yorePhone>/timezone=<yoreTimezone>'
       Returns:
                {
                 "phone_n": "yorePhone",
                 "timezone": "yoreTimezone"
                 }
  
     PUT: '/update_client/phone=<phone_n>/timezone=<timezone>'\
       Returns:
               {
                  "phone_n": "yorePhone",
                 "timezone": "yoreTimezone"
               }
  
      DELETE: '/delete_client/phone=<yorePhone>'
        Returns:
               {
                 "phone_n": "yorePhone",
                 "delete": "Successfully"
               }
  
  Mailing:
  
     POST: '/add_mailing/mailing_name=<yoreMailing>/phone_number=<yorePhone>/message=<yoreMessage>'
        Returns:
               {
                  "ml_name": "yoreMailing", 
                  "phone_n": "yorePhone", 
                  "message": "yoreMessage"
                }
  
     PUT: '/update_mailing/mailing_name=<yoreMailing>/phone=<yorePhone>/message=<yoreMessage>'
        Returns:
               {
                  "ml_name": "yoreMailing", 
                  "phone_n": "yorePhone", 
                  "message": "yoreMessage"
                }
  
      DELETE: '/delete_mailing/mailing_name=<yoreMailing>'
        Returns:
               {
                 "ml_name": "yoreMailing", 
                }
  
   Message:
   
      POST: '/add_message/message=<yoreMessage>'
         Returns:
               {
                 "message": "yoreMessage", 
                 "added": "True", 
               }
  
     DELETE: '/delete_message/message=<message_>'
        Returns:
                {
                  "message": "yoreMessage", 
                  "deleted": "True", 
                }
  
   All mailing stats:
   
      GET: '/all_mailing_stats'
         Returns:
                {
                }

   Detail mailing stats:
   
      GET: '/detail_mailing_stats/mailing=<mailing_mame>'
         Returns:
               {
               }
   Mass mailing:
   
       GET: '/mass_mailing/mail=<mailing_mame>'
         Returns:
            if correct request:
                {
                "if 200 all is ok": 200
                }
