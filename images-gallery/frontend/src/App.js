import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import Search from './components/Search';
import ImageCard from './components/ImageCard';
import { Container, Row, Col } from 'react-bootstrap';
import Welcome from './components/Welcome';
const UNSPLASH_KEY = process.env.REACT_APP_UNSPLASH_KEY;

const App = () => {
  const [word, setWord] = useState('');
  const [images, setImages] = useState([]);

  console.log(images);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    fetch(
      // `https://api.unsplash.com/photos/random?query=${encodeURIComponent(word)}&client_id=${UNSPLASH_KEY}&count=10`,)
      `https://api.unsplash.com/photos/random?query=${encodeURIComponent(word)}&client_id=${UNSPLASH_KEY}`,
    )
      // `https://api.unsplash.com/photos/search?query=${encodeURIComponent(word)}&client_id=${UNSPLASH_KEY},)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setImages([{ ...data, title: word }, ...images]);
        console.log(images);
      })
      .catch((err) => console.log(err));

    setWord('');
  };

  const handleDeleteImage = (id) => {
    setImages(images.filter((image) => image.id !== id));
  };

  return (
    <div>
      <Header title="Images Gallery" />
      <Search word={word} setWord={setWord} handleSubmit={handleSearchSubmit} />
      <Container className="mt-4">
        {images.length ? (
          <Row xs={1} md={3} lg={3}>
            {images.map((image, i) => (
              <Col key={i} className="pb-3">
                <ImageCard image={image} deleteImage={handleDeleteImage} />
              </Col>
            ))}
          </Row>
        ) : (
          <Welcome />
        )}
      </Container>
    </div>
  );
};

export default App;
