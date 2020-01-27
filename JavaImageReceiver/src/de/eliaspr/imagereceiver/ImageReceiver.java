package de.eliaspr.imagereceiver;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class ImageReceiver {

    public static void main(String[] args) throws IOException {
        DatagramSocket socket = new DatagramSocket(32127);
        byte[] buffer = new byte[4096];
        DatagramPacket packet = new DatagramPacket(buffer, 4096);
        while (true) {
            socket.receive(packet);
            int imageSizeBytes = SerializationUtils.readInt(buffer, 0);
            int imagePacketCount = SerializationUtils.readInt(buffer, 4);
            byte[] imageBuffer = new byte[imageSizeBytes];
            for (int i = 0; i < imagePacketCount; i++) {
                socket.receive(packet);
                int packetIndex = SerializationUtils.readInt(buffer, 0);
                int packetSize = SerializationUtils.readInt(buffer, 4);
                int packetOffset = packetIndex * 4000;
                System.arraycopy(buffer, 8, imageBuffer, packetOffset, packetSize);
            }

            BufferedImage image = ImageIO.read(new ByteArrayInputStream(imageBuffer));
            JOptionPane.showMessageDialog(null, "Test,", "Test", JOptionPane.INFORMATION_MESSAGE, new ImageIcon(image));
        }
    }
// 48645321
}
