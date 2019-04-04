class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = [0] * (input_size + 1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr

    def activation_fn(self, x):
        #print( " x=", x)
        #funcao binaria
        return 1 if x >= 0 else 0

        #funcao bipolar
        # return 1 if x >= 0 else -1



    def weighted_sum(self, x, w):
        if(len(x) != len(w)):
            raise Exception("List with differents sizes")
        r = 0
        for i in range(len(w)):
            r += x[i] * w[i]
        return r

    def predict(self, x):
        z = self.weighted_sum(self.W, x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(len(d)):
                x = [1] + X[i]
                y = self.predict(x)
                e = d[i] - y
                for j  in range(len(self.W)):
                    self.W[j] = self.W[j] + self.lr * e * x[j]


class Network(object):
    """Implements a perceptron network"""
    def __init__(self, input_size = 2):
        print("Componentes: ")
        self.perceptron_and = self.train_perceptron_and(input_size)
        self.perceptron_or = self.train_perceptron_or(input_size)
        self.perceptron_not = self.train_perceptron_not()
    
    def train_perceptron_and(self, input_size):
        X = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
        d = [0, 0, 0, 1]

        perceptron_and = Perceptron(input_size)
        perceptron_and.fit(X, d)
        # print("The W results for AND = ",perceptron_and.W)
        
        testes = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]

        print("Teste da componente AND:")
        for t in testes:
            x = [1] + t
            print("\t", x[1], " AND ", x[2], " = ", perceptron_and.predict(x))
        
        return perceptron_and
      
    def train_perceptron_or(self, input_size):
        X = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
        d = [0, 1, 1, 1]

        perceptron_or = Perceptron(input_size)
        perceptron_or.fit(X, d)
        # print("The W results OR = ",perceptron_or.W)

        
        testes = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]

        print("Teste da componente OR:")
        for t in testes:
            x = [1] + t
            print("\t", x[1], " OR ", x[2], " = ", perceptron_or.predict(x))
        
        return perceptron_or
    
    
    def train_perceptron_not(self):
        X = [
                [0],
                [1],
            ]
        d = [1, 0]

        input_size = 1
        perceptron_not = Perceptron(input_size)
        perceptron_not.fit(X, d)
        # print("The W results = ",perceptron_not.W)

        testes = [
            [0],
            [1]
        ]

        print("Teste da componente NOT:")
        for t in testes:
            x = [1] + t
            print("\t NOT", x[1], " = ", perceptron_not.predict(x))
            
        return perceptron_not
      

    def predict(self, first_value, second_value):
        predict_first_and = self.perceptron_and.predict([1, first_value, second_value])
        predict_not = self.perceptron_not.predict([1, predict_first_and])
        predict_or = self.perceptron_or.predict([1, first_value, second_value])
        return self.perceptron_and.predict([1, predict_not, predict_or])


n = Network()

print("-------------------------------XOR-------------------------------")
print("Teste da rede XOR: ")

print("\t 0 XOR 0 = ", n.predict(0, 0))
print("\t 0 XOR 1 = ", n.predict(0, 1))
print("\t 1 XOR 0 = ", n.predict(1, 0))
print("\t 1 XOR 1 = ", n.predict(1, 1))

# print("Digite o primeiro valor do XOR:")
# first_value = int(input())

# print("Digite o segundo valor do XOR:")
# second_value = int(input())

# print(first_value, " XOR ", second_value, " = ", n.predict(first_value, second_value))