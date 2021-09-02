class CurrencyNormalizer:
    @staticmethod
    def normalize(data):
        result = []

        for key in data:
            result.append({
                'code': key,
                'title': data[key]
            })

        return result
