-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 23, 2017 at 11:44 PM
-- Server version: 5.6.34-log
-- PHP Version: 7.1.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blogz`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `body` varchar(5000) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`id`, `title`, `body`, `user_id`) VALUES
(1, 'So it goes...', 'The most important thing I learned on Tralfamadore was that when a person dies he only appears to die. He is still very much alive in the past, so it is very silly for people to cry at his funeral. All moments, past, present and future, always have existed, always will exist. The Tralfamadorians can look at all the different moments just that way we can look at a stretch of the Rocky Mountains, for instance. They can see how permanent all the moments are, and they can look at any moment that interests them. It is just an illusion we have here on Earth that one moment follows another one, like beads on a string, and that once a moment is gone it is gone forever.\r\n\r\nWhen a Tralfamadorian sees a corpse, all he thinks is that the dead person is in bad condition in that particular moment, but that the same person is just fine in plenty of other moments. Now, when I myself hear that somebody is dead, I simply shrug and say what the Tralfamadorians say about dead people, which is \"So it goes.\"', 1),
(2, 'Sandpipers', 'There were little sandpipers running along the margin of the shore which seemed to have this problem: they needed to find their food in the sand which a wave had just washed over, but they couldn\'t bear to get their feet wet. To deal with this problem they ran with an odd kind of movement as if they\'d been constructed by somebody very clever in Switzerland.', 2),
(3, 'Beach House', 'A beach house isn\'t just real estate. It\'s a state of mind.\r\nA beach house doesn\'t even have to be on the beach. Though the best ones are. We all like to congregate at boundary conditions.\r\nWhere land meets water. Where earth meets air. Where body meets mind. Where space meets time. We like to be on one side, and look at the other.', 2),
(4, 'Fart Around!', 'I tell you, we are here on Earth to fart around, and don\'t let anybody tell you different.', 3),
(5, 'Be Soft', 'Do not let the world make you hard. \r\nDo not let pain make you hate.\r\nDo not let the bitterness steal your sweetness.\r\nTake pride that even though the rest of the world may disagree, you still believe it to be a beautiful place.', 3),
(6, 'SCIENCE!', 'Science is magic that works.', 3),
(7, 'Peculiar Travel Suggestions', 'Peculiar travel suggestions are dancing lessons from god.', 4),
(8, 'Pretending to Understand', 'Tiger got to hunt,\r\nBird got to fly;\r\nMan got to sit and wonder, \"Why, why, why?\"\r\nTiger got to sleep,\r\nBird got to land;\r\nMan got to tell himself he understand.', 4);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(40) DEFAULT NULL,
  `pw_hash` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `pw_hash`) VALUES
(1, 'billy_pilgrim', 'ec05e2ae4e7c673743bfd2a64723f8cfdaf7748cd1e8e10bc652f29d0e40acf6,yCkCr'),
(2, 'wonko_the_sane', '66cc6edb2a92a4911b7618e559f7aaec3425436cbeea9192b06e0436e784c21d,JCYAb'),
(3, 'k_vonnegut5', '123e8642e537221b705f2bb89055227aa1be8ca6a3c844c778f1c898d621da57,upnPz'),
(4, 'bokonon', '57c6ba97acc288afb6c01b0a92797f261ee10826a3ec682bb9b00cd3dcb97c5b,ZNUVY');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `blog`
--
ALTER TABLE `blog`
  ADD CONSTRAINT `blog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
