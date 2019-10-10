from marshmallow_dataclass import dataclass
import json
import urllib.request


@dataclass
class Point:
	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon

	lat: float
	lon: float


@dataclass
class City:
	def __init__(self, id, name, coord, country):
		self.id = id
		self.name = name
		self.coord = coord
		self.country = country

	id: int
	name: str
	coord: Point
	country: str


def main():
	contents = urllib.request.urlopen(
		"https://samples.openweathermap.org/data/2.5/forecast?q="
		"M%C3%BCnchenDE&appid=b6907d289e10d714a6e88b30761fae22"
	).read()
	doc_str = json.loads(contents)
	print(json.dumps(doc_str, indent=4, sort_keys=True))
	city_str = doc_str["city"]
	city = City.Schema().loads(str(city_str).replace("\'", "\""))
	print(city)


if __name__ == "__main__":
	main()
