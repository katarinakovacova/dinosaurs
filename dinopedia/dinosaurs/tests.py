from django.test import TestCase, Client
from .models import Dinosaur


class DinosaurTestCase(TestCase):
    def setUp(self):
        Dinosaur.objects.create(
            name="Spinosaurus",
            eating_classification=Dinosaur.EatingClassification.CARNIVORE,
            typical_color="green")

        Dinosaur.objects.create(
            name="Velociraptor", 
            eating_classification=Dinosaur.EatingClassification.CARNIVORE, 
            typical_color="brown", 
            period=Dinosaur.Period.CRETACEOUS)

    def test_dinosaurs_create(self):
        spinosaurus = Dinosaur.objects.get(name="Spinosaurus")
        self.assertEqual(spinosaurus.name, "Spinosaurus")
        self.assertEqual(spinosaurus.eating_classification, Dinosaur.EatingClassification.CARNIVORE)
        self.assertEqual(spinosaurus.typical_color, "green")
        self.assertEqual(spinosaurus.period, Dinosaur.Period.UNKNOWN)
        self.assertEqual(spinosaurus.average_size, Dinosaur.Size.UNKNOWN)
        self.assertFalse(spinosaurus.image1)
        self.assertFalse(spinosaurus.image2)

        velociraptor = Dinosaur.objects.get(name="Velociraptor")
        self.assertEqual(velociraptor.name, "Velociraptor")
        self.assertEqual(velociraptor.eating_classification, Dinosaur.EatingClassification.CARNIVORE)
        self.assertEqual(velociraptor.typical_color, "brown")
        self.assertEqual(velociraptor.period, Dinosaur.Period.CRETACEOUS)
        self.assertEqual(velociraptor.average_size, Dinosaur.Size.UNKNOWN)
        self.assertFalse(velociraptor.image1)
        self.assertFalse(velociraptor.image2)

    def test_dinosaurs_api(self):
        client = Client()
        response = client.get("/api/v1/dinosaurs")
        self.assertEqual(response.status_code, 200)
        dinosaurs = response.json()
        self.assertEqual(len(dinosaurs), 2)

    def test_dinosaur_api(self):
        client = Client()
        response = client.get("/api/v1/dinosaurs")
        self.assertEqual(response.status_code, 200)
        dinosaurs = response.json()

        velociraptor = next(dinosaur for dinosaur in dinosaurs if dinosaur["name"] == "Velociraptor")
        velociraptor_id = velociraptor["id"]

        response = client.get(f"/api/v1/dinosaurs/{velociraptor_id}/")
        self.assertEqual(response.status_code, 200)
        dinosaur = response.json()

        self.assertEqual(dinosaur["name"], "Velociraptor")
        self.assertEqual(dinosaur["eating_classification"], "C")
        self.assertEqual(dinosaur["typical_color"], "brown")
        self.assertEqual(dinosaur["period"], "C")
        self.assertEqual(dinosaur["average_size"], "U")
        self.assertFalse(dinosaur["image1"])
        self.assertFalse(dinosaur["image2"])
