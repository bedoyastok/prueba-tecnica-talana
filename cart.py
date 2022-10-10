import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner


class ShoppingCart(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
      cls.driver = webdriver.Chrome(ChromeDriverManager().install())
      driver = cls.driver
      driver.get("http://automationpractice.com/index.php")
      driver.maximize_window()
   
   #Given el usuario quiere añadir mas de un producto al carro de compras
   #When selecciona los productos
   #Then se deben ver la cantidad exacta de productos en el carrito

   def test_add_fisrt_item(self):
      driver = self.driver
      item_1 = driver.find_element(By.LINK_TEXT, "Faded Short Sleeve T-shirts")
      action = ActionChains(driver)
      action.move_to_element(item_1)
      action.perform()

      button_add = driver.find_element(By.LINK_TEXT, "Add to cart")
      button_add.click()
      driver.implicitly_wait(10)

      button_continue = driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')
      button_continue.click()

   def test_add_secod_item(self):
      driver = self.driver
      item_2 = driver.find_element(By.LINK_TEXT, "Blouse")
      action = ActionChains(driver)
      action.move_to_element(item_2)
      action.perform()

      button_add = driver.find_element(By.LINK_TEXT, "Add to cart")
      button_add.click()
      driver.implicitly_wait(10)

      button_continue = driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')
      button_continue.click()
   
   def test_add_third_item(self):
      driver = self.driver
      item_3 = driver.find_element(By.LINK_TEXT, "Printed Dress")
      action = ActionChains(driver)
      action.move_to_element(item_3)
      action.perform()

      button_add = driver.find_element(By.LINK_TEXT, "Add to cart")
      button_add.click()
      driver.implicitly_wait(10)

      button_proceed = driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
      button_proceed.click()

   #Given el usuario quiere hacer checkout y editar su direccion
   #When termina de agregar los items
   #And da click en proceder con el checkout
   #And confirma la compra
   #And realiza el login
   #And edita la direccion
   #And continua con el metodo de pago
   #Then el flujo debe ser normal
   #And la edicion de la direccion no afecta el checkout

   def test_checkout_sign_in(self):
      driver = self.driver
      button_proceed = driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
      button_proceed.click()

      email = driver.find_element(By.ID, "email")
      email.send_keys("bedoya.stok@gmail.com")

      password = driver.find_element(By.ID, "passwd")
      password.send_keys("123456")

      sign_in = driver.find_element(By.ID, "SubmitLogin")
      sign_in.click()
      driver.implicitly_wait(10)
   
   def test_update_address(self):
      driver = self.driver
      button_update = driver.find_element(By.XPATH, '//*[@id="address_delivery"]/li[9]/a/span')
      button_update.click()

      address = driver.find_element(By.ID, "address")
      address.send_keys("calle 50 #10-10")
      submit = driver.find_element(By.ID, "submitAddress")
      submit.click()

      button_proceed = driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button')
      button_proceed.click()

      check = driver.find_element(By.ID, "cgv")
      check.click()

      button_proceed = driver.find_element(By.XPATH, '//*[@id="form"]/p/button')
      button_proceed.click()
      driver.implicitly_wait(10)

   
   #Given el usuario quiere ver el historial de ordenes
   #When finaliza el checkout
   #And ir a mis ordenes
   #Then deben aparecer todas las ordenes de acuerdo a su estado
      
   def test_pay_bank(self):
      driver = self.driver
      pay_bank = driver.find_element(By.CLASS_NAME, "bankwire")
      pay_bank.click()

      button_confirm = driver.find_element(By.XPATH, '//*[@id="cart_navigation"]/button')
      button_confirm.click()
      driver.implicitly_wait(10)

   def test_orders(self):
      driver = self.driver
      my_orders = driver.find_element(By.LINK_TEXT, "My orders")
      my_orders.click()
      driver.implicitly_wait(10)

   @classmethod
   def tearDownClass(cls):
      cls.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'test', report_name = 'shopping-cart'))






