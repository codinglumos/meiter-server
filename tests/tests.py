from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from metierapi.models import Service
from metierapi.models import MetierUser
from rest_framework.response import Response
 
class ServiceTests(APITestCase):
    fixtures = ['users', 'tokens', 'metieruser', 'services', 'comments', 'reactions']
 
    def setUp(self):
 
       self.metier_user = MetierUser.objects.first()
       token = Token.objects.get(user=self.metier_user.user)
       self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
   
    def test_create_service(self):
     
        url = "/services"
        data = {
            "creator": 1,
            "service": "This is watercolor on canvas",
            "image": "ggggg",
            "body": "A beautiful skyline with stars",
            "price": 600,
            "comment": 1,
            "reactions": 1
        }
 
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
        self.assertEqual(json_response["service"], "This is watercolor on canvas")
        self.assertEqual(json_response["image"], "ggggg")
        self.assertEqual(json_response["body"], "A beautiful skyline with stars")
        self.assertEqual(json_response["price"], 600)
        
    def test_change_service(self):
     
        service = Service()
        service.creator_id = 1
        service.price = 229
        service.service = "Coming Out"
        service.image = "https://static.wixstatic.com/media/81fb6c_d04b89ec2e3148968b201c22ec07ed1a~mv2.jpg/v1/crop/x_248,y_85,w_1414,h_1451/fill/w_293,h_300,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/IMG_5287_edited.jpg"
        service.body = "LGBTQ Painting- Celebrating Pride"
        service.publication_date = "2023-01-06"
        service.comment_id = 1
        service.save()
 
        data = {
            "service": "Coming Out!",
            "image": "https://static.wixstatic.com/media/81fb6c_d04b89ec2e3148968b201c22ec07ed1a~mv2.jpg/v1/crop/x_248,y_85,w_1414,h_1451/fill/w_293,h_300,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/IMG_5287_edited.jpg",
            "price": 300,
            "body": "LGBTQ Painting- Celebrating Pride",
        }
 
        response = self.client.put(f"/services/{service.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
        response = self.client.get(f"/services/{service.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
        self.assertEqual(json_response["service"], "Coming Out!")
        self.assertEqual(json_response["image"], "https://static.wixstatic.com/media/81fb6c_d04b89ec2e3148968b201c22ec07ed1a~mv2.jpg/v1/crop/x_248,y_85,w_1414,h_1451/fill/w_293,h_300,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/IMG_5287_edited.jpg")
        self.assertEqual(json_response["price"], 300)
        self.assertEqual(json_response["body"], "LGBTQ Painting- Celebrating Pride")
 
   
    def test_get_service(self):
     
        service = Service()
        service.creator_id = 1
        service.service = "Coming Out!"
        service.image = "https://static.wixstatic.com/media/81fb6c_d04b89ec2e3148968b201c22ec07ed1a~mv2.jpg/v1/crop/x_248,y_85,w_1414,h_1451/fill/w_293,h_300,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/IMG_5287_edited.jpg"
        service.body = "LGBTQ Painting- Celebrating Pride"
        service.price = 229
        service.comment_id = 1
        service.publication_date = "2022-02-01"
        service.reactions_id = 1
 
        service.save()
 
     
        response = self.client.get(f"/services/{service.id}")
 
        json_response = json.loads(response.content)
 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
        self.assertEqual(json_response["id"], service.id)
        self.assertEqual(json_response["service"], "Coming Out!")
        self.assertEqual(json_response["body"], "LGBTQ Painting- Celebrating Pride")
        self.assertEqual(json_response["price"], 229)
        self.assertEqual(json_response["image"], "https://static.wixstatic.com/media/81fb6c_d04b89ec2e3148968b201c22ec07ed1a~mv2.jpg/v1/crop/x_248,y_85,w_1414,h_1451/fill/w_293,h_300,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/IMG_5287_edited.jpg")
 
    def test_delete_nonexistent_service_returns_404(self):
     
        response = self.client.delete(f"/services/12345")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
    def test_delete_service(self):
       
        service = Service()
        service.creator_id = 1
        service.price = 67
        service.service = "Cold Nights"
        service.body = "I always feel warm next to you. "
        service.publication_date = "2023-01-06"
        service.image = "https://ctl.s6img.com/society6/img/nQCnw-hQFSDsTsPwVo4_J7-kOzg/w_700/prints/~artwork/s6-original-art-uploads/society6/uploads/misc/29c4c121a0764c82aa84b70822f0f203/~~/cold-nights7805032-prints.jpg"
   
        service.save()
 
        response = self.client.delete(f"/services/{service.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
        response = self.client.get(f"/services/{service.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
